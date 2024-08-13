from datetime import datetime
from typing import Optional

from app.core.services.AppService import AppService
from app.core.services.ServiceResult import ServiceResult
from app.dao.CounterDao import CounterDAO
from app.dao.UrlShorteningDao import UrlShorteningDAO
from app.exceptions.UrlShorteningExceptions import UrlShorteningExceptions
from app.schemas.api.responses.ShortenURLResponseSchema import ShortenURLResponseSchema
from app.utils.convert_base10_to_base58 import convert_base10_to_base58


class UrlShorteningService(AppService):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter_dao_instance = CounterDAO(self.db)
        self.url_shortening_dao_instance = UrlShorteningDAO(self.db)

    def get_current_count(self):
        return self.counter_dao_instance.get_counter("url_shortener", 10 ** 9)

    def __encode(self, num: int) -> str:
        return convert_base10_to_base58(num)

    async def shorten_url(self, original_url: str, expiration_date: Optional[datetime]) -> ServiceResult:
        result = None
        domain = self.settings.CLIENT_HOST
        while result is None:
            counter = self.get_current_count()
            short_url_hash = self.__encode(counter)
            short_url = f"{domain}/{short_url_hash}"
            try:
                result = await self.url_shortening_dao_instance.set_url(original_url, short_url, expiration_date)
            except UrlShorteningExceptions.ShortenedURLAlreadyExist as e:
                self.logger.info(f"Short URL {short_url} already exists. Trying again.")
                pass

        data = ShortenURLResponseSchema(
            original_url=result.original_url,
            short_url=result.short_url,
            expiration_date=result.expiration_date
        )
        return ServiceResult(data)

    async def retrieve_url(self, shorten_url_hash: str) -> ServiceResult:
        domain = self.settings.CLIENT_HOST
        short_url = f"{domain}/{shorten_url_hash}"
        result = await self.url_shortening_dao_instance.retrieve_with_short_url(short_url)
        if not result:
            raise UrlShorteningExceptions.ShortenedURLNotFound()

        data = ShortenURLResponseSchema(
            original_url=result.original_url,
            short_url=result.short_url,
            expiration_date=result.expiration_date
        )

        return ServiceResult(data)
