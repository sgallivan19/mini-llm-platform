from qdrant_client import QdrantClient
from app.core.config import settings

client = QdrantClient(host=settings.qdrant_host, port=settings.qdrant_port)

def ensure_collection():
    try:
        client.get_collection(settings.qdrant_collection)
    except Exception:
        # create with embedding size placeholder 1536
        client.recreate_collection(
            collection_name=settings.qdrant_collection,
            vectors_config={"size":1536, "distance":"Cosine"}
        )

def upsert_documents(vectors: list[dict]):
    client.upsert(collection_name=settings.qdrant_collection, points=vectors)

def qdrant_query(query_text: str, top_k: int = 5):
    from app.services.openai_client import OpenAIClient
    emb = OpenAIClient().embed([query_text])[0]
    res = client.search(collection_name=settings.qdrant_collection, query_vector=emb, top=top_k)
    hits = [{"id": p.id, "score": p.score, "payload": p.payload} for p in res]
    return hits
