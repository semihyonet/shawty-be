from functools import lru_cache

from redis import Redis


@lru_cache
def get_redis_client() -> Redis:
    return Redis(host='localhost', port=6379)


redis_client = get_redis_client()
