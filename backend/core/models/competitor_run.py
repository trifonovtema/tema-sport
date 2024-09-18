import uuid
from datetime import datetime
from typing import Optional, List

from core.models.base import Base
from core.models.run import Run
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Uuid, DateTime

from core.models.finish_run import FinishRun
from core.models.gate_run import GateRun
from core.models.split_run import SplitRun
from core.models.start_run import StartRun


class CompetitorRun(Base):
    competitor_id: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    scheduled_time: Mapped[Optional[datetime]] = mapped_column(DateTime(True))
    run_id: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)

    run: Mapped["Run"] = relationship("Run", back_populates="competitor_runs")
    finishes_runs: Mapped[List["FinishRun"]] = relationship(
        "FinishesRun", back_populates="competitor_run"
    )
    gates_runs: Mapped[List["GateRun"]] = relationship(
        "GateRun", back_populates="competitor_run"
    )
    splits_runs: Mapped[List["SplitRun"]] = relationship(
        "SplitRun", back_populates="competitor_run"
    )
    starts_runs: Mapped[List["StartRun"]] = relationship(
        "StartRun", back_populates="competitor_run"
    )
