from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .user import User
from ...settings import get_settings


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class AccessToken(
    Base, SQLAlchemyBaseAccessTokenTable[get_settings().db.id_type.id_type]
):  # !

    user_id: Mapped[get_settings().db.id_type.id_type] = mapped_column(
        get_settings().db.id_type.id_type_sqlalchemy,
        ForeignKey(User.id, ondelete="cascade"),
        nullable=False,  # GUID,
    )

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyAccessTokenDatabase(session, cls)
