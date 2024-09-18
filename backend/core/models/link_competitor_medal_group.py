from typing import Optional

from core.config import settings
from core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class LinkCompetitorMedalGroup(Base):
    __table_name__ = "link_competitors_medal_groups"
    competitor_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(nullable=True)
    )
    medal_group_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(nullable=True)
    )
