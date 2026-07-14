# AI IT Helpdesk Assistant (RAG)

A retrieval-augmented generation system that answers L1 IT support questions
by retrieving from an internal knowledge base and generating grounded answers
— instead of a static FAQ or a generic chatbot that hallucinates fixes.

**Built by:** Mandar Kadam
**Stack:** Python, FastAPI, ChromaDB, sentence-transformers, Groq (Llama 3.1)

---

## The problem this solves

L1 tickets are dominated by a small set of repeat issues — VPN drops, password
resets, printer failures, Outlook sync. Every one of those already has a
documented fix in the team's SOPs. The bottleneck isn't knowledge, it's
**retrieval speed**: a human has to remember the right doc exists, find it,
and read it, or a junior engineer opens a ticket that a senior engineer then
has to pick up.

This system collapses that gap. A user (or a junior support agent) types the
issue in plain language, the system retrieves the exact relevant SOP section
from a vector database, and an LLM turns it into a direct, step-by-step
answer — with the source doc cited so it's auditable, not a black box.

## How it works

```
User question
     │
     ▼
Embed question (sentence-transformers, local, free)
     │
     ▼
Vector similarity search against KB chunks (ChromaDB)
     │
     ▼
Top-3 relevant SOP chunks retrieved
     │
     ▼
Chunks + question sent to LLM (Groq / Llama 3.1) with instruction:
"answer ONLY from this context, cite the SLA/escalation path if present"
     │
     ▼
Grounded answer + source filename returned to user
```

This is the same pattern (RAG) used in production enterprise tools like
Glean, Microsoft Copilot for Service, and internal help bots at companies
running M365 — the difference here is you can point to the exact code and
explain every layer of it.

## Why this design (talking points for interviews)

- **Grounded, not hallucinated**: the LLM is instructed to answer only from
  retrieved context and say "I don't know, open a ticket" otherwise — this is
  the difference between a toy chatbot and something you'd trust in a real
  service desk.
- **Free to run**: local embeddings (no per-query cost), ChromaDB requires no
  server, Groq's free tier is generous enough for a portfolio demo or small
  team pilot.
- **Source-cited answers**: every response shows which SOP it came from,
  which matters for auditability in an enterprise IT context.
- **Swappable KB**: point `ingest.py` at your real SOPs/KB export and
  re-run — the sample articles here are realistic but are placeholders.

## Setup (local)

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# edit .env and add your free Groq API key from https://console.groq.com

python ingest.py                # builds the vector DB from data/sample_kb/
uvicorn app:app --reload --port 8000
```

Open `http://localhost:8000` — chat UI is served directly from the backend.

## Deploying free (Render)

1. Push this folder to a GitHub repo.
2. On [Render](https://render.com), create a new **Web Service**, connect the repo.
3. Build command: `pip install -r requirements.txt && python ingest.py`
4. Start command: `uvicorn app:app --host 0.0.0.0 --port $PORT`
5. Add environment variable `GROQ_API_KEY` in Render's dashboard.
6. Deploy. Free tier will spin down when idle and cold-start on the next
   request — expected behavior on a free plan, mention this if asked in an
   interview (shows you understand the tradeoff, not that you missed it).

## Swapping in your real KB

Replace the files in `data/sample_kb/` with your own SOPs/KB articles as
`.md` files (plain markdown, use `## ` headers for sections — the chunker
splits on those). Re-run `python ingest.py`. No code changes needed.

## Extending it (next steps if you want to go further)

- Add conversation memory so follow-up questions ("what if that doesn't work?") retain context
- Log every query + answer to a file/DB — gives you a second project: "analyzed helpdesk AI query patterns to find KB gaps"
- Add a feedback thumbs up/down per answer, use it to flag SOPs that need rewriting
- Swap Groq for a locally-run model (Ollama) for a fully offline/on-prem story, relevant if you're targeting orgs with data residency requirements
