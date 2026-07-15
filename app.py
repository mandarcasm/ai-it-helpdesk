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
import json
import time
from datetime import date
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from pydantic import BaseModel
from dotenv import load_dotenv
import chromadb
from chromadb.utils import embedding_functions
from groq import Groq
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

load_dotenv()

DB_DIR = os.path.join(os.path.dirname(__file__), "chroma_db")
COLLECTION_NAME = "it_helpdesk_kb"
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

# Real self-service password reset — this is the actual "automation" for
# password/lockout issues. We deliberately do NOT let the chatbot reset
# passwords itself (unauthenticated chat + password reset = security risk).
# Instead, detect password/lockout/MFA questions and hand off directly to
# Microsoft's own SSPR portal, which does identity verification via MFA.
SSPR_URL = os.environ.get("SSPR_URL", "https://passwordreset.microsoftonline.com")
_PASSWORD_KEYWORDS = {
    "password-reset-lockout.md",
    "mfa-registration-failures.md",
}

# --- Abuse protection for free-tier API credits ---
# Per-IP limit: stops one person/bot hammering the endpoint.
PER_IP_LIMIT = os.environ.get("PER_IP_RATE_LIMIT", "10/hour")
# Global daily cap: stops the free Groq quota being drained even by many
# different IPs (e.g. if the link gets shared or scraped). Resets at midnight
# server time. This is an in-memory counter, intentionally simple for a
# single-instance free-tier deployment — resets on restart, which is fine.
DAILY_GLOBAL_CAP = int(os.environ.get("DAILY_GLOBAL_CAP", "150"))
_daily_count = {"date": date.today().isoformat(), "count": 0}


def _check_and_increment_daily_cap():
    today = date.today().isoformat()
    if _daily_count["date"] != today:
        _daily_count["date"] = today
        _daily_count["count"] = 0
    if _daily_count["count"] >= DAILY_GLOBAL_CAP:
        return False
    _daily_count["count"] += 1
    return True


limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="AI IT Helpdesk Assistant",
    description="Created by MandarK (mandarcasm)",
)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Load vector DB + embedding function once at startup ---
# DefaultEmbeddingFunction uses ChromaDB's bundled ONNX MiniLM model —
# no PyTorch needed, which matters a lot for free-tier hosting memory limits.
embed_fn = embedding_functions.DefaultEmbeddingFunction()
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


def _sse(event_type: str, **payload) -> str:
    """Format one Server-Sent-Events record."""
    return f"data: {json.dumps({'type': event_type, **payload})}\n\n"


def _confidence_from_distance(best_distance: float) -> str:
    """
    Turn ChromaDB's cosine distance for the best-matching chunk into a
    plain confidence label. Cosine distance ranges 0 (identical) to 2
    (opposite) — similarity = 1 - distance. These thresholds are a
    reasonable starting heuristic for MiniLM-scale embeddings, not a
    universal constant; tune them if your own KB content is very short
    or very repetitive.
    """
    similarity = max(0.0, 1 - best_distance)
    if similarity >= 0.55:
        return "high"
    if similarity >= 0.35:
        return "medium"
    return "low"


@app.get("/health")
def health():
    kb_article_count = 0
    if collection is not None:
        try:
            all_meta = collection.get(include=["metadatas"])["metadatas"]
            kb_article_count = len(set(m["source"] for m in all_meta))
        except Exception:
            pass
    return {
        "status": "ok",
        "collection_ready": collection is not None,
        "ticket_url": TICKET_URL,
        "kb_article_count": kb_article_count,
    }


@app.post("/chat")
@limiter.limit(PER_IP_LIMIT)
def chat(request: Request, req: ChatRequest):
    # Pre-flight checks happen BEFORE we start streaming — once a
    # StreamingResponse begins, headers are already sent and we can't
    # cleanly raise an HTTPException anymore.
    if not _check_and_increment_daily_cap():
        raise HTTPException(
            429,
            "This demo has hit its daily usage limit to protect free API credits. "
            "Please try again tomorrow.",
        )
    if collection is None:
        raise HTTPException(500, "Knowledge base not ingested yet. Run ingest.py first.")
    if groq_client is None:
        raise HTTPException(500, "GROQ_API_KEY not set. Add it to your .env file.")
    if not req.question.strip():
        raise HTTPException(400, "Question cannot be empty.")

    def generate():
        results = collection.query(
            query_texts=[req.question],
            n_results=TOP_K,
            include=["documents", "metadatas", "distances"],
        )
        docs = results.get("documents", [[]])[0]
        metas = results.get("metadatas", [[]])[0]
        dists = results.get("distances", [[]])[0]

        if not docs:
            yield _sse(
                "meta", sources=[], ticket_url=TICKET_URL,
                quick_action_url=None, quick_action_label=None, confidence="low",
            )
            yield _sse(
                "chunk",
                text="I couldn't find anything in our help articles that matches "
                     "this. Please raise a ticket so a real person can help you out.",
            )
            yield _sse("done")
            return

        context = "\n\n---\n\n".join(docs)
        sources = sorted(set(m["source"] for m in metas))
        confidence = _confidence_from_distance(min(dists)) if dists else "low"

        quick_action_url = None
        quick_action_label = None
        if _PASSWORD_KEYWORDS & set(sources):
            quick_action_url = SSPR_URL
            quick_action_label = "🔑 Reset Your Password Now (self-service, no ticket needed)"

        # Send metadata first so the frontend can render sources/buttons
        # immediately, before any answer text has streamed in.
        yield _sse(
            "meta", sources=sources, ticket_url=TICKET_URL,
            quick_action_url=quick_action_url, quick_action_label=quick_action_label,
            confidence=confidence,
        )

        stream = groq_client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"CONTEXT:\n{context}\n\nQUESTION: {req.question}"},
            ],
            temperature=0.2,
            max_tokens=500,
            stream=True,
        )
        for piece in stream:
            delta = piece.choices[0].delta.content
            if delta:
                yield _sse("chunk", text=delta)

        yield _sse("done")

    return StreamingResponse(generate(), media_type="text/event-stream")


# --- Serve the frontend ---
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/")
def serve_index():
    return FileResponse(os.path.join(static_dir, "index.html"))


@app.get("/architecture")
def serve_architecture():
    return FileResponse(os.path.join(static_dir, "architecture.html"))
