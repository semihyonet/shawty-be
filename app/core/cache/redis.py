from functools import lru_cache

from redis import Redis

from app.core.settings import get_settings


@lru_cache
def get_redis_client() -> Redis:
    settings = get_settings()
    return Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)


redis_client = get_redis_client()
