from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel
from app.services.ingest_service import submit_ingest_job
from app.services.chat_service import chat_with_retrieval
from app.services.embed_service import embed_texts
from app.services.rerank_service import rerank_candidates
from app.core.config import settings
from fastapi import FastAPI
from app.core.security import APIKeyMiddleware

router = APIRouter()

class IngestRequest(BaseModel):
    documents: list[str]
    metadata: dict | None = None

class ChatRequest(BaseModel):
    query: str

class EmbedRequest(BaseModel):
    texts: list[str]

class RerankRequest(BaseModel):
    query: str
    candidates: list[dict]

@router.post("/ingest")
async def ingest(req: IngestRequest):
    job_id = await submit_ingest_job(req.documents, req.metadata)
    return {"job_id": job_id}

@router.post("/chat")
async def chat(req: ChatRequest):
    answer = await chat_with_retrieval(req.query)
    return {"answer": answer}

@router.post("/embed")
async def embed(req: EmbedRequest):
    embs = embed_texts(req.texts)
    return {"embeddings": embs}

@router.post("/rerank")
async def rerank(req: RerankRequest):
    ranked = rerank_candidates(req.query, req.candidates)
    return {"ranked": ranked}
