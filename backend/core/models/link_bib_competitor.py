from typing import Optional

from core.config import settings
from core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class LinkBibCompetitor(Base):
    __tablename__ = "link_bibs_competitors"

    bib_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = mapped_column(
        nullable=True
    )
    competitor_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(nullable=True)
    )
