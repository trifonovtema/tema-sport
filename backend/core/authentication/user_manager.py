from __future__ import annotations

from typing import TYPE_CHECKING


from fastapi_users import BaseUserManager, IntegerIDMixin  # UUIDIDMixin

from backend.core.models import User
from ..types.user_id import UserIdType
from ...settings import get_settings
import logging

if TYPE_CHECKING:
    from fastapi import Request

logger = logging.getLogger(__name__)

settings = get_settings()


class UserManager(IntegerIDMixin, BaseUserManager[User, UserIdType]):
    reset_password_token_secret = settings.access_token.reset_password_token_secret
    verification_token_secret = settings.access_token.verification_token_secret

    async def on_after_register(self, user: User, request: Request | None = None):
        logger.warning("User %r has registered.", user.id)

    async def on_after_forgot_password(
        self, user: User, token: str, request: Request | None = None
    ):
        logger.warning(
            "User %r has forgot their password. Reset token: %r",
            user.id,
            token,
        )

    async def on_after_request_verify(
        self, user: User, token: str, request: Request | None = None
    ):
        logger.warning(
            "Verification requested for user %r. Verification token: %r",
            user.id,
            token,
        )
