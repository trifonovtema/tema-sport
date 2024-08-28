from fastapi import APIRouter

from backend.core.schemas.user import UserRead, UserUpdate
from backend.base_api.api.v1.fastapi_users_router import fastapi_users
from backend.settings import get_settings

settings = get_settings()
router = APIRouter(
    prefix=settings.base_api.v1.users,
    tags=["Users"],
)
#/me , /{id}
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
)
