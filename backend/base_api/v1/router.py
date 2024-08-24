from fastapi import APIRouter
from backend.base_api.v1.users.router import router as router_user
from backend.base_api.v1.competitions.router import router as router_competition

from backend.base_api.v1.router_websocket import router as router_websocket

router = APIRouter(prefix="/v1")
router.include_router(router_user)
router.include_router(router_competition)
router.include_router(router_websocket)


@router.get("/health", summary="Check Health", description="Check health desc")
async def get_health():
    return {"health": "ok"}
