import pytz
import datetime
from typing import Optional

from app.core.services.AppDao import AppDAO
from app.exceptions.UrlShorteningExceptions import UrlShorteningExceptions
from app.models import ShortenUrlModel


class UrlShorteningDAO(AppDAO):
    async def retrieve_with_short_url(self, short_url: str) -> Optional[ShortenUrlModel]:
        now = datetime.datetime.now(pytz.utc)
        return await ShortenUrlModel.find(
            ShortenUrlModel.short_url == short_url,
            ShortenUrlModel.expiration_date > now
        ).first_or_none()

    async def set_url(self, url: str, short_url: str, expiration_date: datetime.datetime) -> ShortenUrlModel:
        shortened_url = await self.retrieve_with_short_url(short_url)
        if shortened_url is not None:
            raise UrlShorteningExceptions.ShortenedURLAlreadyExist()

        model = ShortenUrlModel(original_url=url, short_url=short_url, expiration_date=expiration_date)
        await model.insert()

        return model
