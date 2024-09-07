from typing import TYPE_CHECKING

from .base import Base
from .mixins.id_pk import IdPkMixin
from ..SQLAlchemyDatabases.competition import SQLAlchemyCompetitionDatabase
from core.config import settings
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class Competition(Base):
    if TYPE_CHECKING:  # pragma: no cover
        id: settings.db.id_type_class.get_id_type()
        name: str
    else:
        name: Mapped[str] = mapped_column(
            String(length=4000), unique=True, index=True, nullable=False
        )

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyCompetitionDatabase(session, cls)
