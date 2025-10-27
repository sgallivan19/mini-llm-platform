from celery import Celery
from app.core.config import settings

celery_app = Celery(
    "worker",
    broker=settings.celery_broker,
    backend=settings.celery_backend,
)

celery_app.conf.task_routes = {
    "app.workers.tasks.ingest_documents_task": {"queue": "ingest"}
}
