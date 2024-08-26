from fastapi import APIRouter

from backend.core.schemas.user import UserRead, UserCreate
from backend.dependencies.authentication.backend import authentication_backend
from backend.base_api.v1.fastapi_users_router import fastapi_users
from backend.settings import get_settings

settings = get_settings()
router = APIRouter(
    prefix=settings.base_api.v1.auth,
    tags=["Auth"],
)

# /login and /logout
router.include_router(
    fastapi_users.get_auth_router(
        authentication_backend,
    ),
    prefix="/jwt",
)
# /register
router.include_router(
    fastapi_users.get_register_router(
        UserRead,
        UserCreate,
    ),
)
