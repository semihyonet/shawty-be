from fastapi import APIRouter

from app.api.health_router import health_router

main_router = APIRouter(prefix="/api/v1")

main_router.include_router(health_router)
