import uuid
from app.workers.tasks import ingest_documents_task

async def submit_ingest_job(documents: list[str], metadata: dict | None):
    job_id = str(uuid.uuid4())
    ingest_documents_task.delay(job_id, documents, metadata or {})
    return job_id
