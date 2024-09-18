from datetime import datetime
from typing import Optional, List, TYPE_CHECKING

from core.config import settings
from core.models.competitor import Competitor
from core.models.base import Base
from core.models.run import Run
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Uuid, DateTime, ForeignKey

if TYPE_CHECKING:
    from core.models.link_finish_competitor_run import LinkFinishCompetitorRun
    from core.models.link_gate_competitor_run import LinkGateCompetitorRun
    from core.models.link_split_competitor_run import LinkSplitCompetitorRun
    from core.models.link_start_competitor_run import LinkStartCompetitorRun


class CompetitorRun(Base):
    __tablename__ = "competitor_runs"

    competitor_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(ForeignKey(Competitor.id))
    )
    scheduled_time: Mapped[Optional[datetime]] = mapped_column(DateTime(True))
    run_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = mapped_column(
        ForeignKey(Run.id)
    )

    run: Mapped["Run"] = relationship("Run", back_populates="competitor_runs")

    finishes_runs: Mapped[List["LinkFinishCompetitorRun"]] = relationship(
        "LinkFinishCompetitorRun", back_populates="competitor_run"
    )
    gates_runs: Mapped[List["LinkGateCompetitorRun"]] = relationship(
        "LinkGateCompetitorRun", back_populates="competitor_run"
    )
    splits_runs: Mapped[List["LinkSplitCompetitorRun"]] = relationship(
        "LinkSplitCompetitorRun", back_populates="competitor_run"
    )
    starts_runs: Mapped[List["LinkStartCompetitorRun"]] = relationship(
        "LinkStartCompetitorRun", back_populates="competitor_run"
    )
