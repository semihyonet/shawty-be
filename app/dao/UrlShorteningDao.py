import pytz
import datetime
from typing import Optional

from beanie.odm.operators.find.logical import Or

from app.core.services.AppDao import AppDAO
from app.exceptions.UrlShorteningExceptions import UrlShorteningExceptions
from app.models import ShortenUrlModel
from app.services.CacheService import UrlCacheService


class UrlShorteningDAO(AppDAO):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cache_service = UrlCacheService()

    async def retrieve_with_short_url(self, short_url: str) -> Optional[ShortenUrlModel]:
        now = datetime.datetime.now(pytz.utc)

        cached_url = await self.cache_service.get(short_url)
        if cached_url is not None and (cached_url.expiration_date is None or now < cached_url.expiration_date):
            return cached_url

        return await ShortenUrlModel.find(
            ShortenUrlModel.short_url == short_url,
            Or(ShortenUrlModel.expiration_date == None, ShortenUrlModel.expiration_date > now)
        ).first_or_none()

    async def set_url(self, url: str, short_url: str, expiration_date: Optional[datetime.datetime]) -> ShortenUrlModel:
        shortened_url = await self.retrieve_with_short_url(short_url)
        if shortened_url is not None:
            raise UrlShorteningExceptions.ShortenedURLAlreadyExist()

        model = ShortenUrlModel(original_url=url, short_url=short_url, expiration_date=expiration_date)
        await model.insert()
        self.cache_service.set(short_url, model)

        return model
