from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    APP_NAME: str = "Multi-Agent Research Engine"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "production"
    LOG_LEVEL: str = "INFO"

    OPENAI_API_KEY: Optional[str] = "mock-key"
    ANTHROPIC_API_KEY: Optional[str] = "mock-key"
    SERPAPI_API_KEY: Optional[str] = "mock-key"

    MAX_SEARCH_RESULTS: int = 5
    MAX_REVISION_CYCLES: int = 2

    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()
