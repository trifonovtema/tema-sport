from datetime import datetime
from typing import Optional, TYPE_CHECKING

from core.config import settings
from core.models.finish import Finish
from core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, ForeignKey
from core.models.competitor_run import CompetitorRun

# if TYPE_CHECKING:


class LinkFinishCompetitorRun(Base):
    __tablename__ = "link_finishes_competitor_runs"

    finish_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(
            ForeignKey(Finish.id),
            nullable=True,
        )
    )
    competitor_run_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(
            ForeignKey(CompetitorRun.id),
            nullable=True,
        )
    )

    finish_time: Mapped[Optional[datetime]] = mapped_column(DateTime)

    competitor_run: Mapped["CompetitorRun"] = relationship(
        "CompetitorRun", back_populates="finishes_runs"
    )
