#!/usr/bin/env bash
set -e
# run DB migrations (if any)
if [ -f "alembic.ini" ]; then
  alembic upgrade head || true
fi
# ensure qdrant collection exists by calling a small python helper
python - <<'PY'
from app.utils.qdrant_client import ensure_collection
ensure_collection()
print("prestart: ensured qdrant collection")
PY
# finally start the app
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
