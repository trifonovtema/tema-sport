from datetime import datetime
from typing import Optional

from core.config import settings
from core.models import BaseTable
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime

from core.models.competitor_run import CompetitorRun


class SplitRun(BaseTable):
    __tablename__ = "splits_runs"

    split_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = mapped_column(
        nullable=True
    )
    competitor_run_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(nullable=True)
    )
    split_time: Mapped[Optional[datetime]] = mapped_column(DateTime)

    competitor_run: Mapped["CompetitorRun"] = relationship(
        "CompetitorRun", back_populates="splits_runs"
    )
