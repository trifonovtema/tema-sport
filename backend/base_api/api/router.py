from fastapi import APIRouter
from .v1.router import router as router_api_v1
from backend.settings import get_settings

router = APIRouter(
    prefix=get_settings().base_api.prefix,
)
router.include_router(router_api_v1)
