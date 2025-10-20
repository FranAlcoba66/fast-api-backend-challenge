from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import    Field
from functools import lru_cache
from typing import List, Optional

class Settings(BaseSettings):
    # Application
    APP_NAME: str
    APP_ENV: str
    BACKEND_HOST: str
    BACKEND_PORT: int

    # Database
    DATABASE_URL: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    # API
    PROJECT_NAME: str
    VERSION: str
    API_V1_STR: str

    # Security
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # Database pool settings
    DB_POOL_SIZE: int
    DB_MAX_OVERFLOW: int
    DB_POOL_TIMEOUT: int
    DB_POOL_RECYCLE: int
    #
    POKEMON_API_URL: str
    # CORS
    BACKEND_CORS_ORIGINS: List[str]
    ALLOWED_ORIGINS: str = Field(default="http://localhost:3000")
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore"
    )

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
