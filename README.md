# Mini LLM Platform (Starter) - Enhanced Zip

Quickstart:
1. Copy `.env.example` -> `.env` and fill secrets.
2. `docker compose up --build`
3. `curl -H "x-api-key: ${API_KEY}" http://localhost:8000/chat -d '{"query":"hello"}' -H "Content-Type: application/json"`

This repo is a starter scaffold (FastAPI + Qdrant + Postgres + Redis + Celery + OpenAI).
