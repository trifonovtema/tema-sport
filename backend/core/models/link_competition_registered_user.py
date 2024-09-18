from typing import Optional

from core.config import settings
from core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text


class LinkCompetitionRegisteredUser(Base):
    __tablename__ = "link_competitions_registered_users"
    user_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = mapped_column(
        nullable=True
    )
    competition_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(nullable=True)
    )
    type: Mapped[Optional[str]] = mapped_column(Text)
