"""
Ingestion pipeline: reads all .md files from data/sample_kb/, chunks them,
embeds them with a local sentence-transformer model, and stores them in
a persistent ChromaDB collection.

Run this once initially, and again any time you add/update KB articles:
    python ingest.py
"""

import os
import glob
import chromadb
from chromadb.utils import embedding_functions

KB_DIR = os.path.join(os.path.dirname(__file__), "data", "sample_kb")
DB_DIR = os.path.join(os.path.dirname(__file__), "chroma_db")
COLLECTION_NAME = "it_helpdesk_kb"

# Free, local, no API key needed. Runs on CPU fine for this scale.
EMBED_MODEL = "all-MiniLM-L6-v2"


def chunk_markdown(text: str, filename: str, max_chars: int = 900):
    """
    Chunk by markdown ## sections first (keeps each SOP step-group intact),
    falling back to fixed-size chunks if a section is too long.
    """
    sections = text.split("\n## ")
    chunks = []
    for i, section in enumerate(sections):
        content = section if i == 0 else "## " + section
        content = content.strip()
        if not content:
            continue
        if len(content) <= max_chars:
            chunks.append(content)
        else:
            # fallback: split long sections into ~max_chars windows
            for j in range(0, len(content), max_chars):
                chunks.append(content[j:j + max_chars])
    return chunks


def main():
    print(f"Loading embedding model '{EMBED_MODEL}' (first run downloads it, ~80MB)...")
    embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=EMBED_MODEL
    )

    client = chromadb.PersistentClient(path=DB_DIR)

    # Fresh collection each run to avoid stale/duplicate chunks
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass
    collection = client.create_collection(
        name=COLLECTION_NAME, embedding_function=embed_fn
    )

    files = sorted(glob.glob(os.path.join(KB_DIR, "*.md")))
    if not files:
        print(f"No .md files found in {KB_DIR}. Add KB articles and re-run.")
        return

    ids, docs, metadatas = [], [], []
    for filepath in files:
        filename = os.path.basename(filepath)
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
        chunks = chunk_markdown(text, filename)
        for idx, chunk in enumerate(chunks):
            ids.append(f"{filename}::{idx}")
            docs.append(chunk)
            metadatas.append({"source": filename})

    collection.add(ids=ids, documents=docs, metadatas=metadatas)
    print(f"Ingested {len(docs)} chunks from {len(files)} files into '{COLLECTION_NAME}'.")
    print(f"Vector DB persisted at: {DB_DIR}")


if __name__ == "__main__":
    main()
