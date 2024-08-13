from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    IS_DEBUG: bool

    REDIS_HOST: str
    REDIS_PORT: str

    SECRET_KEY: str

    MONGODB_URL: str
    MONGODB_DB_NAME: str

    HOST: str
    CLIENT_HOST: str

    class Config:
        if Path('.env').exists():
            env_file = '.env'
            env_file_encoding = 'utf-8'


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
