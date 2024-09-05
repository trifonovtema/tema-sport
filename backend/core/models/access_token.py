from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .user import User
from backend.core.config import settings


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class AccessToken(
    Base,
    SQLAlchemyBaseAccessTokenTable[settings.db.id_type_class.get_id_type()],
):
    user_id: Mapped[settings.db.id_type_class.get_id_type()] = mapped_column(
        settings.db.id_type_class.get_sqlalchemy_type(),
        ForeignKey(User.id, ondelete="cascade"),
        nullable=False,  # GUID,
    )

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyAccessTokenDatabase(session, cls)
