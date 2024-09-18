from datetime import datetime
from typing import Optional, TYPE_CHECKING

from core.config import settings
from core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime


if TYPE_CHECKING:
    from core.models.competitor_run import CompetitorRun


class FinishRun(Base):
    __tablename__ = "finishes_runs"

    finish_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(nullable=True)
    )
    competitor_run_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(nullable=True)
    )
    finish_time: Mapped[Optional[datetime]] = mapped_column(DateTime)

    competitor_run: Mapped["CompetitorRun"] = relationship(
        "CompetitorRun", back_populates="finishes_runs"
    )
