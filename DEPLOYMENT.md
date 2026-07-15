# Deployment Guide — AI IT Helpdesk Assistant

**Created by MandarK (mandarcasm)**

This is a field-tested deployment guide. Every issue below is something that
actually happened setting this project up on Windows — not a hypothetical
troubleshooting list. If you hit an error, check here before searching
elsewhere; it's probably already documented.

---

## Before you start: environment checklist

- [ ] Windows 10/11, admin rights on your machine
- [ ] ~1GB free disk space
- [ ] A free [Groq](https://console.groq.com) account for your API key
- [ ] A free [GitHub](https://github.com) account
- [ ] A free [Render](https://render.com) account for hosting

---

## Part 1 — Local setup, step by step

1. Install **Python 3.11.9** specifically (see "Do's and Don'ts" below for
   why the version matters). Check "Add python.exe to PATH" during install.
2. Extract this project, open a terminal in the project folder.
3. `python -m venv venv`
4. `venv\Scripts\activate` (Windows) — prompt should show `(venv)`.
5. `pip install -r requirements.txt` — takes 1-3 minutes, well under 1GB (no PyTorch — this project uses a lightweight ONNX embedding model instead).
6. `copy .env.example .env`, then edit `.env` and add your real
   `GROQ_API_KEY` (get one free at console.groq.com).
7. `python ingest.py` — builds the vector database from `data/sample_kb/`.
   Should end with `Ingested X chunks from 50 files`.
8. `uvicorn app:app --reload --port 8000` — open `http://localhost:8000`.

---

## Part 2 — Every real issue we hit, and the actual fix

### Issue: `pip install` fails with a numpy/meson build error on Windows

**What it looks like:** A wall of red text ending in something like
`Unknown compiler(s)` and `metadata-generation-failed`, mentioning `meson`
and `numpy`.

**Root cause:** You're running Python 3.13. Several packages in this
project (numpy, torch, etc.) don't ship precompiled installers for 3.13 yet,
so pip tries to compile them from source — which requires a C compiler
(Visual Studio Build Tools) that almost nobody has installed.

**Fix:** Don't install a compiler to force it through. Install
**Python 3.11.9** instead, recreate your virtual environment with it, and
reinstall. Prebuilt packages exist for 3.11, so nothing needs to compile.

---

### Issue: Python 3.11 has no Windows installer on the newer release pages

**What it looks like:** You go to install a newer Python 3.11.x patch (like
3.11.15) and the release page only offers a "Source release" — no
`.exe` installer.

**Root cause:** Python 3.11 entered "security fixes only" mode. Past a
certain patch version, only source releases are published — no binaries.

**Fix:** Use **Python 3.11.9** specifically — the last 3.11 patch with a
full Windows installer. It shows a "superseded" notice on python.org;
ignore that notice, it's irrelevant for this purpose.

---

### Issue: `python --version` says "not recognized" after installing

**What it looks like:** Install appears to finish successfully, but any new
terminal says `python : The term 'python' is not recognized...`

**Root cause:** The installer's "Add python.exe to PATH" checkbox wasn't
checked, or PATH changes hadn't propagated to already-open terminals.

**Fix:**
1. Open System Properties → Environment Variables → System variables → `Path` → Edit.
2. Add both `C:\Python311` and `C:\Python311\Scripts` as new entries.
3. Close **every** open terminal window completely.
4. Open a fresh terminal and re-test.

Environment variable changes never apply to already-open terminals — this
trips people up constantly.

---

### Issue: `TypeError: Client.__init__() got an unexpected keyword argument 'proxies'`

**What it looks like:** Server crashes on startup with this exact error,
deep in a stack trace involving `groq/_base_client.py` and `httpx`.

**Root cause:** A version mismatch between the pinned `groq` package and a
newer `httpx` that got installed alongside it — an older Groq client version
passes a `proxies` argument that newer httpx versions removed.

**Fix:** `pip install --upgrade groq`. This project's `requirements.txt` is
already fixed to pin `groq>=1.5.0`, so a fresh install won't hit this — but
if you're troubleshooting an existing broken environment, the upgrade
command is the direct fix.

---

### Issue: Chat says "Could not reach the backend" but the frontend loads fine

**Root cause:** The frontend (`static/index.html`) is a static file — it
loads regardless of whether the backend server is actually running. This
error specifically means the FastAPI server (`uvicorn`) isn't running, isn't
finished starting, or crashed after a code change.

**Fix:** Check the terminal running `uvicorn` directly — don't just look at
the browser. Look for the actual error text, not just "it's not working."

---

### Issue: You edited `.env` but the app still says the key is missing / KB still looks like the old version

**Root cause:** Two separate but similar traps —
1. `.env` changes require a **server restart** (Ctrl+C, then rerun
   `uvicorn`) — hot-reload does not re-read environment variables.
2. Editing `data/sample_kb/*.md` files does **not** update the running
   assistant — the vector database (`chroma_db/`) is a separate, cached copy
   built from those files. You must delete `chroma_db/` and rerun
   `python ingest.py` after any KB content change, every time.

---

### Issue: Free hosting costs money unexpectedly / API credits vanish fast

**Root cause:** A publicly reachable chatbot with no rate limiting can be
hit by bots, scrapers, or just heavy sharing, burning through a free LLM API
quota in hours.

**Fix:** This project has two protections built in — a per-IP rate limit
(`PER_IP_RATE_LIMIT`, default 10/hour) and a global daily cap
(`DAILY_GLOBAL_CAP`, default 150/day), both set as environment variables at
deploy time. Set these on Render alongside your API key. Never deploy a
public LLM-backed endpoint without some form of rate limiting.

---

## Part 3 — Render deployment issues (separate from local ones above)

Everything in Part 2 happens on your own machine. These happen specifically
once you deploy to Render — different environment, different failure modes,
even though some *look* similar to the local issues.

### Issue: Build fails with a `pydantic-core` / metadata-generation error on Render

**What it looks like:** Nearly identical to the local numpy build failure —
`metadata-generation-failed`, mentions `pydantic-core`, build exits status 1.

**Root cause:** Same root cause as the local numpy issue, different
package. Render defaults new services to a very recent Python version
(3.14 at time of writing) unless told otherwise, and some pinned
dependencies don't have prebuilt wheels for it yet.

**Fix:** Pin Python explicitly for Render — add a file named
`.python-version` to your repo root containing just:
```
3.11.9
```
Also set `PYTHON_VERSION=3.11.9` as an environment variable on Render as a
backup (both methods are officially supported; using both is just extra
reliability). Commit the file, then trigger a fresh deploy.

---

### Issue: Deploy fails with "Ran out of memory (used over 512MB)"

**What it looks like:** Build succeeds, deploy starts, logs show the app
apparently starting, then it just dies with this exact memory message.

**Root cause:** Render's free tier caps every service at 512MB RAM. Loading
PyTorch plus a sentence-transformers embedding model easily exceeds that —
PyTorch alone can use several hundred MB just to import, before your app
has done anything. This works fine locally because most machines have far
more than 512MB free.

**Fix:** Stop using PyTorch-based embeddings entirely. ChromaDB ships a
lightweight embedding function (`DefaultEmbeddingFunction`, an ONNX version
of MiniLM-L6-v2) that does the same job using a fraction of the memory —
this project uses it in both `ingest.py` and `app.py`. Also remove
`sentence-transformers` from `requirements.txt` (it drags in PyTorch and
several GB of NVIDIA packages as dependencies) and add `onnxruntime`
explicitly instead. This is the single most impactful fix for running any
embedding-based AI project on a free-tier host.

---

### Issue: "Port scan timeout reached, no open ports detected"

**What it looks like:** After a deploy, logs show repeated "No open ports
detected, continuing to scan..." messages, eventually giving up with this
timeout error.

**Root cause:** This is usually a *symptom*, not the actual problem. Render
expects your app to bind to a network port so it can receive traffic. If
your app crashes on startup for any reason (like the memory error above),
it never gets the chance to bind a port — so Render just keeps waiting,
then eventually reports "no port found." Always check for a crash
**earlier** in the same logs before treating this as a standalone issue.

**Fix:** Find and fix the actual crash (check for OOM errors, import
errors, or unhandled exceptions higher up in the log). Once the app starts
successfully, port binding resolves itself — there's nothing to configure
for this specifically as long as the app uses `--host 0.0.0.0 --port $PORT`
in its start command, which this project already does.

---

### Issue: A fresh deploy still shows the old error, even after pushing a fix

**What it looks like:** You fix the code, push to GitHub, trigger a deploy,
and it fails with the exact same error as before.

**Root cause:** Usually one of two things — either the push happened
*after* the deploy had already started building (so it built the old
commit), or the fix wasn't actually committed the way you thought (verify,
don't assume).

**Fix:** Before troubleshooting further, open the actual file on GitHub's
website (not your local copy) and read its real content. Compare the
commit timestamp to when the failing deploy started. If your fix landed
after the deploy started, just trigger one more deploy — it'll pick up the
right commit this time.

---

### Note (not a bug): First response after inactivity takes 30-70+ seconds

**What it looks like:** The site loads, but the first question you ask
takes much longer to answer than every question after it.

**Root cause:** Two separate, stacking delays on the free tier — (1) the
instance itself spins down after 15 minutes idle and takes ~30-60s to wake
up, and (2) the ONNX embedding model (~79MB) downloads into a runtime cache
on the *first* request after a cold start, since the build-time cache
doesn't carry over. Both are one-time costs per cold start, not per
message.

**Fix:** Nothing to fix — this is expected free-tier behavior. Worth
explaining confidently if asked about it (shows you understand the
infrastructure tradeoff), rather than treating it as a bug. Paid Render
tiers eliminate the spin-down but cost money.

---

## Do's and Don'ts

### Do
- **Do** use Python 3.11.9 for this project specifically — it's the version everything here was tested against.
- **Do** delete and rebuild `chroma_db/` every time you change files in `data/sample_kb/`.
- **Do** restart the server after any `.env` change.
- **Do** set rate limits (`PER_IP_RATE_LIMIT`, `DAILY_GLOBAL_CAP`) before making a deployment public.
- **Do** keep your real API key only in `.env` locally and in Render's environment variables when deployed — never in a file that gets committed to git.
- **Do** test locally before every deploy — never push straight to Render without confirming it runs on your machine first.
- **Do** read the actual terminal output when something breaks, not just the browser's generic error message.
- **Do** pin your Python version explicitly on every hosting platform you deploy to (`.python-version` file and/or `PYTHON_VERSION` env var) — don't rely on a platform's default.
- **Do** use lightweight, non-PyTorch alternatives (like ONNX-based embeddings) when deploying AI/ML projects to free-tier hosting with memory limits.
- **Do** verify a fix actually landed on GitHub (open the real file, check the commit timestamp) before assuming a redeploy will include it.
- **Do** check earlier in a log file for the root cause when you see a generic downstream error like a port timeout — it's often a symptom of something that failed a few lines up.

### Don't
- **Don't** install the newest Python version by default — check what a project actually needs first. Newest isn't always compatible.
- **Don't** install a full C++ compiler toolchain just to force a source build through — if pip is trying to compile something, it's almost always a version mismatch, not a real requirement.
- **Don't** commit `.env` to git, ever. It's already in `.gitignore` — keep it that way.
- **Don't** grant an unauthenticated chatbot the ability to reset passwords, unlock accounts, or take any action requiring identity verification — hand off to a real verified system (like SSPR) instead.
- **Don't** assume editing a source file (KB article, config) automatically updates the running app — most components here need an explicit rebuild or restart step.
- **Don't** deploy a public API-backed endpoint without rate limiting, even for a portfolio demo.
- **Don't** assume a hosting platform's default Python/runtime version matches what you tested locally — pin it explicitly every time.
- **Don't** default to PyTorch-based ML libraries for a free-tier deployment without checking the memory budget first — lighter alternatives usually exist.
- **Don't** trust that a push "probably worked" — open the file on the actual platform (GitHub, in this case) and read it.

---

## Quick reference — commands used throughout this project

```bash
# Local setup
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python ingest.py
uvicorn app:app --reload --port 8000

# After changing KB articles
Remove-Item -Recurse -Force chroma_db
python ingest.py

# After changing .env
# (Ctrl+C the running server, then:)
uvicorn app:app --reload --port 8000

# Fixing a stuck/broken venv
Remove-Item -Recurse -Force venv
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**Render-specific files this project relies on:**
- `.python-version` — pins Python to 3.11.9 on Render (and locally, if your tooling respects it)
- `requirements.txt` — uses `onnxruntime` instead of `sentence-transformers`/PyTorch specifically to fit Render's free-tier 512MB memory limit
- Environment variables set in Render's dashboard (not in any file): `GROQ_API_KEY`, `TICKET_URL`, `DAILY_GLOBAL_CAP`, `PYTHON_VERSION`

---

*Document maintained by MandarK (mandarcasm) as part of the AI IT Helpdesk Assistant portfolio project.*
