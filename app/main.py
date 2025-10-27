from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router
from app.core.config import settings
from app.core.security import APIKeyMiddleware
from app.utils.qdrant_client import ensure_collection

app = FastAPI(title="Mini LLM Platform")
# Public health endpoint stays open (H1)
app.include_router(api_router, prefix="")

@app.on_event("startup")
async def startup_event():
    # ensure qdrant collection exists on startup
    try:
        ensure_collection()
    except Exception as e:
        print("startup: ensure_collection failed:", e)

@app.get("/health")
async def health():
    return {"status": "ok", "service": "mini-llm-platform"}
