from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from base_api.api.v1.users.router_auth import router as router_auth
from base_api.api.v1.users.router_users import router as router_users
from base_api.api.v1.runs.router import router as router_runs
from base_api.api.v1.races.router import router as router_races

# from base_api.api.v1.router_websocket import router as router_websocket
from core.config import settings

http_bearer = HTTPBearer(auto_error=False)


router = APIRouter(
    prefix=settings.api.v1.prefix,
    dependencies=[Depends(http_bearer)],
)
# router.include_router(router_user)
# router.include_router(router_competition)
# router.include_router(router_websocket)
router.include_router(router_auth)
router.include_router(router_users)
router.include_router(router_runs)
router.include_router(router_races)
