from fastapi import APIRouter

from backend.settings import get_settings

settings = get_settings()
router = APIRouter(
    prefix=settings.base_api.v1.auth,
    tags=["Auth"],
)


@router.get("/health", summary="Check Health", description="Check health desc")
async def get_health():
    return {"health": "ok"}
