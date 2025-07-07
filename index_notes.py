from pathlib import Path
import re, uuid, nltk, markdown
from nltk.tokenize import sent_tokenize
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

# ------------------- CONFIG -------------------
NOTES_DIR     = Path("my_notes")
COLLECTION    = "note_chunks"
EMBED_MODEL   = "nomic-ai/nomic-embed-text-v1"
CHUNK_TOKENS  = 200
BATCH_SIZE    = 1_000
# ----------------------------------------------

nltk.download("punkt")

embedder = SentenceTransformer(EMBED_MODEL, trust_remote_code=True)
client   = QdrantClient(host="localhost", port=6333)

client.recreate_collection(
    collection_name=COLLECTION,
    vectors_config=models.VectorParams(
        size=embedder.get_sentence_embedding_dimension(),
        distance=models.Distance.COSINE
    )
)

def md_to_chunks(path: Path):
    """Yield ~CHUNK_TOKENS-sized plain-text chunks."""
    html   = markdown.markdown(path.read_text(encoding="utf-8", errors="ignore"))
    text   = re.sub(r"<[^>]+>", "", html)                 # strip HTML tags
    sents  = sum((sent_tokenize(p) for p in text.splitlines()), [])
    buf, tokens = [], 0
    for s in sents:
        t = s.split()
        tokens += len(t); buf.append(s)
        if tokens >= CHUNK_TOKENS:
            yield " ".join(buf)
            buf, tokens = [], 0
    if buf:
        yield " ".join(buf)

def make_point(note_name: str, chunk_id: int, text: str):
    return models.PointStruct(
        id=str(uuid.uuid4()),
        payload={"note": note_name, "chunk_id": chunk_id, "text": text},
        vector=embedder.encode(f"passage: {text}", normalize_embeddings=True)
    )

batch, total = [], 0
for note in tqdm(sorted(NOTES_DIR.glob("*.md")), desc="Indexing notes"):
    for idx, chunk in enumerate(md_to_chunks(note)):
        batch.append(make_point(note.name, idx, chunk))
        if len(batch) >= BATCH_SIZE:
            client.upsert(collection_name=COLLECTION, points=batch)
            total += len(batch)
            batch.clear()
# flush remainder
if batch:
    client.upsert(collection_name=COLLECTION, points=batch)
    total += len(batch)

print(f"Indexed {total} chunks into Qdrant ✨")