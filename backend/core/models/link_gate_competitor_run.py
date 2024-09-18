from typing import Optional, TYPE_CHECKING

from core.config import settings
from core.models.athlete import Athlete
from core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey
from core.models.competitor_run import CompetitorRun

# if TYPE_CHECKING:


class LinkGateCompetitorRun(Base):
    __tablename__ = "link_gates_competitor_runs"

    gate_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = mapped_column(
        nullable=True
    )
    competitor_run_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(
            ForeignKey(CompetitorRun.id),
            nullable=True,
        )
    )
    penalty: Mapped[Optional[int]] = mapped_column(Integer)
    athlete_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(
            ForeignKey(Athlete.id),
            nullable=True,
        )
    )

    competitor_run: Mapped["CompetitorRun"] = relationship(
        "CompetitorRun", back_populates="gates_runs"
    )
