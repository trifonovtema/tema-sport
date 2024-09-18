from typing import Optional, TYPE_CHECKING

from core.config import settings
from core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer

if TYPE_CHECKING:
    from core.models.competitor_run import CompetitorRun


class GateRun(Base):
    __tablename__ = "gates_runs"

    gate_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = mapped_column(
        nullable=True
    )
    competitor_run_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(nullable=True)
    )
    penalty: Mapped[Optional[int]] = mapped_column(Integer)
    athlete_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(nullable=True)
    )

    competitor_run: Mapped["CompetitorRun"] = relationship(
        "CompetitorRun", back_populates="gates_runs"
    )
