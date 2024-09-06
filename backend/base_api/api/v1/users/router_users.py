from fastapi import APIRouter

from backend.core.schemas.user import UserRead, UserUpdate
from backend.base_api.api.v1.users.fastapi_users_router import fastapi_users
from backend.core.config import settings


router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["Users"],
)
# /me , /{id}
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
)
