from typing import TYPE_CHECKING, Optional

from fastapi_users import BaseUserManager

from backend.core.models import User
from ...settings import get_settings
import logging

if TYPE_CHECKING:
    from fastapi import Request

logger = logging.getLogger(__name__)


class UserManager(
    get_settings().db.id_type.id_mixin,
    BaseUserManager[User, get_settings().db.id_type.id_type],
):
    reset_password_token_secret = (
        get_settings().access_token.reset_password_token_secret
    )
    verification_token_secret = get_settings().access_token.verification_token_secret

    async def on_after_register(self, user: User, request: Optional["Request"] = None):
        logger.warning("User %r has registered.", user.id)

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional["Request"] = None
    ):
        logger.warning(
            "User %r has forgot their password. Reset token: %r",
            user.id,
            token,
        )

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional["Request"] = None
    ):
        logger.warning(
            "Verification requested for user %r. Verification token: %r",
            user.id,
            token,
        )
