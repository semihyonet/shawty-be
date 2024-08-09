from fastapi import APIRouter

health_router = APIRouter(prefix="", tags=['Basic Router'])

@health_router.get("/health")
async def get_health():
    return {'status': 'OK'}
