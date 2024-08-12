import json
from typing import Optional

from app.core.cache.redis import get_redis_client
from app.core.settings import get_settings
from app.models import ShortenUrlModel


class UrlCacheService:
    def __init__(self, cache_key: str = "shawty/"):
        self.cache_key = cache_key
        self.settings = get_settings()
        self.cache = get_redis_client()

    async def get(self, key) -> Optional[ShortenUrlModel]:
        result = self.cache.get(self.cache_key + key)
        if not result:
            return None
        result_dict = json.loads(result)
        return ShortenUrlModel(**result_dict)

    def set(self, key: str, value: ShortenUrlModel):
        self.cache[self.cache_key + key] = value.model_dump_json()
