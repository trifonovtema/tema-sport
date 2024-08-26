from fastapi import APIRouter
from backend.base_api.v1.users.router import router as router_user
from backend.base_api.v1.competitions.router import router as router_competition
from .router_auth import router as router_auth
from backend.base_api.v1.router_websocket import router as router_websocket
from ...settings import get_settings

settings = get_settings()
router = APIRouter(prefix=settings.base_api.v1.prefix)
router.include_router(router_user)
router.include_router(router_competition)
router.include_router(router_websocket)
router.include_router(router_auth)
