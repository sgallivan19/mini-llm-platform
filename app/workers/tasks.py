from .celery_app import celery_app
from app.services.openai_client import OpenAIClient
from app.utils.qdrant_client import upsert_documents, ensure_collection

@celery_app.task(bind=True)
def ingest_documents_task(self, job_id: str, documents: list, metadata: dict):
    ensure_collection()
    client = OpenAIClient()
    embeddings = client.embed(documents)
    vectors = []
    for i, emb in enumerate(embeddings):
        vectors.append({
            "id": f"{job_id}-{i}",
            "vector": emb,
            "payload": {"text": documents[i], "meta": metadata}
        })
    upsert_documents(vectors)
    return {"job_id": job_id, "ingested": len(vectors)}
