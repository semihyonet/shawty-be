from fastapi import APIRouter

from app.core.database.get_pymongo import get_pymongo
from app.core.utils.result_handler import result_handler
from app.schemas.api.requests.ShortenURLRequestSchema import ShortenURLRequestSchema
from app.schemas.api.responses.ShortenURLResponseSchema import ShortenURLResponseSchema
from app.services.UrlShorteningService import UrlShorteningService

url_shortener_router = APIRouter(prefix="/url-shortener", tags=['URL Shortener'])


@url_shortener_router.post("/shorten", summary="Shorten a URL", response_model=ShortenURLResponseSchema)
async def shorten_url(request: ShortenURLRequestSchema) -> ShortenURLResponseSchema:
    db = get_pymongo()

    service = UrlShorteningService(db)

    response = await service.shorten_url(request.url, request.expiration_date)

    return result_handler(response)


@url_shortener_router.get("/retrieve/{short_url_hash}", summary="Retrieve a URL", response_model=ShortenURLResponseSchema)
async def retrieve_shortened_url(short_url_hash: str) -> ShortenURLResponseSchema:
    db = get_pymongo()

    service = UrlShorteningService(db)

    response = await service.retrieve_url(short_url_hash)

    return result_handler(response)
