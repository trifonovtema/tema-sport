from typing import Optional, List

from core.config import settings
from core.models import BaseTable
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Text


class RaceStage(BaseTable):
    # __table_args__ = (
    #     ForeignKeyConstraint(
    #         ["parent_race_stage_id"],
    #         ["tema_sport.race_stages.id"],
    #         name="race_stages_race_stages_id_fk",
    #     ),
    #     PrimaryKeyConstraint("id", name="race_stages_pk"),
    #     {"schema": "tema_sport"},
    # )

    race_class_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(nullable=True)
    )
    runs_number: Mapped[Optional[int]] = mapped_column(Integer)
    athletes_start_interval: Mapped[Optional[int]] = mapped_column(Integer)
    parent_race_stage_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(nullable=True)
    )
    type: Mapped[Optional[str]] = mapped_column(Text)
    scoring_rule_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(nullable=True)
    )
    athletes_qualified_count: Mapped[Optional[int]] = mapped_column(Integer)
    athletes_qualified_percentage: Mapped[Optional[int]] = mapped_column(Integer)

    parent_race_stage: Mapped["RaceStage"] = relationship(
        "RaceStage",
        remote_side="RaceStage.id",
        back_populates="parent_race_stage_reverse",
    )
    parent_race_stage_reverse: Mapped[List["RaceStage"]] = relationship(
        "RaceStage",
        remote_side=[parent_race_stage_id],
        back_populates="parent_race_stage",
    )
