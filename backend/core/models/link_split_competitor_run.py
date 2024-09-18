from datetime import datetime
from typing import Optional, TYPE_CHECKING

from core.config import settings
from core.models import Split
from core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, ForeignKey
from core.models.competitor_run import CompetitorRun

# if TYPE_CHECKING:


class LinkSplitCompetitorRun(Base):
    __tablename__ = "link_splits_competitor_runs"

    split_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = mapped_column(
        ForeignKey(Split.id),
        nullable=True,
    )
    competitor_run_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(
            ForeignKey(CompetitorRun.id),
            nullable=True,
        )
    )
    split_time: Mapped[Optional[datetime]] = mapped_column(DateTime)

    competitor_run: Mapped["CompetitorRun"] = relationship(
        "CompetitorRun", back_populates="splits_runs"
    )
