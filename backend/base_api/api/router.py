from fastapi import APIRouter
from .v1.router import router as router_api_v1
from backend.core.config import settings

router = APIRouter(
    prefix=settings.api.prefix,
)
router.include_router(router_api_v1)
