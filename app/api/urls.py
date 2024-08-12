from fastapi import APIRouter

from app.api.health_router import health_router
from app.api.url_shortener_router import url_shortener_router

main_router = APIRouter(prefix="/api/v1")

main_router.include_router(health_router)
main_router.include_router(url_shortener_router)