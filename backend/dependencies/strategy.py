from __future__ import annotations
from typing import TYPE_CHECKING, Annotated
from fastapi import Depends
from fastapi_users.authentication.strategy.db import DatabaseStrategy

from .access_tokens import get_access_tokens_db
from ..settings import get_settings

if TYPE_CHECKING:
    from ..core.models import AccessToken
    from fastapi_users.authentication.strategy.db import AccessTokenDatabase

settings = get_settings()


def get_database_strategy(
    access_tokens_db: Annotated[
        AccessTokenDatabase[AccessToken], Depends(get_access_tokens_db)
    ],
) -> DatabaseStrategy:
    return DatabaseStrategy(
        database=access_tokens_db,
        lifetime_seconds=settings.access_token.lifetime_seconds,
    )
