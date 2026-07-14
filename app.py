"""
FastAPI backend for the AI IT Helpdesk Assistant.

Flow per request:
  1. Embed the user's question (same local model used at ingestion time)
  2. Retrieve top-k relevant KB chunks from ChromaDB
  3. Pass question + retrieved context to an LLM (Groq, free tier)
  4. Return the answer + which KB source(s) it came from

Run locally:
    uvicorn app:app --reload --port 8000

Requires a .env file with:
    GROQ_API_KEY=your_key_here
(get a free key at https://console.groq.com)
"""

import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv
import chromadb
from chromadb.utils import embedding_functions
from groq import Groq

load_dotenv()

DB_DIR = os.path.join(os.path.dirname(__file__), "chroma_db")
COLLECTION_NAME = "it_helpdesk_kb"
EMBED_MODEL = "all-MiniLM-L6-v2"
GROQ_MODEL = "llama-3.1-8b-instant"  # fast + free-tier friendly
TOP_K = 3

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# Link shown to the user when they need to escalate to a human.
# Default is a mailto: link so this works out of the box with zero setup.
# Replace with your real ticketing system URL (Zendesk, Freshservice, ServiceNow, etc.)
# by setting TICKET_URL in your .env file.
TICKET_URL = os.environ.get(
    "TICKET_URL",
    "mailto:helpdesk@solstice-tech.example?subject=IT%20Support%20Request",
)

app = FastAPI(title="AI IT Helpdesk Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Load vector DB + embedding function once at startup ---
embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMBED_MODEL)
chroma_client = chromadb.PersistentClient(path=DB_DIR)

try:
    collection = chroma_client.get_collection(name=COLLECTION_NAME, embedding_function=embed_fn)
except Exception:
    collection = None  # will error clearly on first query if ingest.py hasn't been run

groq_client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None

SYSTEM_PROMPT = """You are a friendly IT help assistant for employees who are NOT technical. \
Assume the person you're talking to does not know what a terminal, command line, registry, \
or admin settings are, and has never heard of tools like ipconfig, netsh, or Print Spooler.

Answer using ONLY the SOP context provided below, but TRANSLATE it:
- Rewrite technical steps into plain, everyday actions ("restart your Wi-Fi" not "toggle the \
adapter"; "close the app completely and reopen it" not "kill the process").
- Number the steps simply, and keep each one short — one action per step.
- If a step in the source material genuinely requires admin access, a command line, or IT-only \
tools (e.g. registry edits, spooler restarts, driver rollbacks), do NOT explain how to do it. \
Instead say plainly: "This step needs IT to do for you — please raise a ticket and mention: \
[the specific issue]" so the ticket already has useful context.
- Never use jargon without immediately explaining it in plain words if you must use a technical \
term at all.
- Keep the tone calm and reassuring, like a patient coworker, not a manual.
- If the context includes an SLA, mention roughly how long a fix should take in plain terms \
("IT usually sorts this within a few hours") instead of quoting SLA codes like P2/P3.
- If the context doesn't cover the question, say so plainly and tell them to raise a ticket — \
don't guess or invent steps.
- End every answer with a short, friendly line letting them know they can raise a ticket if \
this doesn't fix it."""


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str
    sources: list[str]
    ticket_url: str


@app.get("/health")
def health():
    return {"status": "ok", "collection_ready": collection is not None, "ticket_url": TICKET_URL}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    if collection is None:
        raise HTTPException(500, "Knowledge base not ingested yet. Run ingest.py first.")
    if groq_client is None:
        raise HTTPException(500, "GROQ_API_KEY not set. Add it to your .env file.")
    if not req.question.strip():
        raise HTTPException(400, "Question cannot be empty.")

    results = collection.query(query_texts=[req.question], n_results=TOP_K)
    docs = results.get("documents", [[]])[0]
    metas = results.get("metadatas", [[]])[0]

    if not docs:
        return ChatResponse(
            answer="I couldn't find anything in our help articles that matches this. "
                   "Please raise a ticket so a real person can help you out.",
            sources=[],
            ticket_url=TICKET_URL,
        )

    context = "\n\n---\n\n".join(docs)
    sources = sorted(set(m["source"] for m in metas))

    completion = groq_client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"CONTEXT:\n{context}\n\nQUESTION: {req.question}"},
        ],
        temperature=0.2,
        max_tokens=500,
    )
    answer = completion.choices[0].message.content

    return ChatResponse(answer=answer, sources=sources, ticket_url=TICKET_URL)


# --- Serve the frontend ---
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/")
def serve_index():
    return FileResponse(os.path.join(static_dir, "index.html"))
