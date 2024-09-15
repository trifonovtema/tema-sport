from typing import TYPE_CHECKING, List

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from . import AccessToken
from .basetable import BaseTable
from core.config import settings
from sqlalchemy.orm import Mapped, relationship

from .competition_owner import CompetitionOwner
from .user_profile import UserProfile

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(
    BaseTable,
    SQLAlchemyBaseUserTable[settings.db.id_type_class.get_id_type()],
):

    access_tokens: Mapped[List["AccessToken"]] = relationship(
        "AccessToken",
        back_populates="user",
    )
    competition_owners: Mapped[List["CompetitionOwner"]] = relationship(
        "CompetitionOwner",
        back_populates="user",
    )
    user_profiles: Mapped[List["UserProfile"]] = relationship(
        "UserProfile",
        back_populates="user",
    )

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
