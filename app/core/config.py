from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    openai_api_key: str
    api_key: str
    postgres_user: str = "postgres"
    postgres_password: str = "postgres"
    postgres_db: str = "llm_platform"
    postgres_host: str = "db"
    postgres_port: int = 5432
    redis_host: str = "redis"
    redis_port: int = 6379
    qdrant_host: str = "qdrant"
    qdrant_port: int = 6333
    qdrant_collection: str = "docs"
    celery_broker: str = "redis://redis:6379/0"
    celery_backend: str = "redis://redis:6379/1"

    # ✅ New-style config (replaces class Config)
    model_config = SettingsConfigDict(
        env_file=".env",      # Load from .env file if present
        env_file_encoding="utf-8",
        extra="ignore"        # Ignore unexpected env vars
    )

settings = Settings()
