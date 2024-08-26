from typing import Annotated

from fastapi import APIRouter, Depends

from backend.core.models import User
from backend.core.schemas.user import UserRead, UserCreate
from backend.dependencies.authentication.backend import authentication_backend
from backend.base_api.api.v1.fastapi_users_router import (
    fastapi_users,
    current_user,
    current_super_user,
)
from backend.settings import get_settings

settings = get_settings()
router = APIRouter(
    prefix=settings.base_api.v1.auth,
    tags=["Auth"],
)

# /login and /logout
router.include_router(
    fastapi_users.get_auth_router(
        backend=authentication_backend,
        # requires_verification=True,
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

# /request-verify-token
# /verify
router.include_router(
    fastapi_users.get_verify_router(UserRead),
)

# /forgot-password (the user asks for a token to reset its password) and /reset-password
router.include_router(
    fastapi_users.get_reset_password_router(),
)


@router.get("/custom_user")
async def custom_user(
    user: Annotated[
        User,
        Depends(current_user),
    ],
):
    return {"user": user}


@router.get("/custom_super_user")
async def custom_super_user(
    user: Annotated[
        User,
        Depends(current_super_user),
    ],
):
    return {"user": user}
