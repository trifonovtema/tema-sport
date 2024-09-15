from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .basetable import BaseTable
from .user import User
from core.config import settings
from sqlalchemy.orm import relationship


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class AccessToken(
    SQLAlchemyBaseAccessTokenTable[settings.db.id_type_class.get_id_type()],
    BaseTable,
):
    user_id: Mapped[settings.db.id_type_class.get_id_type()] = mapped_column(
        settings.db.id_type_class.get_sqlalchemy_type(),
        ForeignKey(User.id, ondelete="cascade"),
        nullable=False,  # GUID,
    )

    user: Mapped["User"] = relationship("User", back_populates="access_tokens")

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyAccessTokenDatabase(session, cls)
