from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from backend.core.types.user_id import UserIdType
from .user import User

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[UserIdType]):  # !

    user_id: Mapped[UserIdType] = mapped_column(
        Integer, ForeignKey(User.id, ondelete="cascade"), nullable=False  # GUID,
    )

    @classmethod
    def get_db(cls, session: AsyncSession):
        return SQLAlchemyAccessTokenDatabase(session, cls)
