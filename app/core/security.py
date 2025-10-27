from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.config import settings

class APIKeyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # allow open health check
        if request.url.path == '/health':
            return await call_next(request)
        api_key = request.headers.get('x-api-key')
        if not api_key or api_key != settings.api_key:
            raise HTTPException(status_code=401, detail='Unauthorized')
        return await call_next(request)
