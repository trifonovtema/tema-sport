from typing import TYPE_CHECKING, List

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from core.models import Base
from core.config import settings
from sqlalchemy.orm import Mapped, relationship

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from core.models import UserProfile
    from core.models import AccessToken
    from core.models.link_competition_owner import LinkCompetitionOwner


class User(
    Base,
    SQLAlchemyBaseUserTable[settings.db.id_type_class.get_id_type()],
):

    access_tokens: Mapped[List["AccessToken"]] = relationship(
        "AccessToken",
        back_populates="user",
    )
    competition_owners: Mapped[List["LinkCompetitionOwner"]] = relationship(
        "LinkCompetitionOwner",
        back_populates="user",
    )
    user_profiles: Mapped[List["UserProfile"]] = relationship(
        "UserProfile",
        back_populates="user",
    )

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
