from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from backend.base_api.api.v1.users.router_auth import router as router_auth
from backend.base_api.api.v1.users.router_users import router as router_users
from backend.base_api.api.v1.router_websocket import router as router_websocket
from backend.core.config import settings

http_bearer = HTTPBearer(auto_error=False)


router = APIRouter(
    prefix=settings.base_api.v1.prefix,
    dependencies=[Depends(http_bearer)],
)
# router.include_router(router_user)
# router.include_router(router_competition)
router.include_router(router_websocket)
router.include_router(router_auth)
router.include_router(router_users)
