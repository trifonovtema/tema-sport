from typing import Optional, TYPE_CHECKING

from .base import Base
from core.config import settings
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from sqlalchemy.orm import relationship
from typing import List

if TYPE_CHECKING:
    from .base import Base
    from .course_element import CourseElement


# class Race(BaseTable):
#     if TYPE_CHECKING:  # pragma: no cover
#         id: settings.db.id_type_class.get_id_type()
#         competition_id: settings.db.id_type_class.get_id_type() | None
#         name: str | None
#     else:
#         name: Mapped[str] = mapped_column(
#             index=True,
#             nullable=False,
#         )
#         competition_id: Mapped[settings.db.id_type_class.get_id_type()] = mapped_column(
#             nullable=True,
#         )


class Race(Base):
    # __tablename__ = "races"
    # __table_args__ = (
    #     PrimaryKeyConstraint("id", name="pk_races"),
    #     Index("ix_tema_sport_races_name", "name"),
    #     {"schema": "tema_sport"},
    # )

    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    competition_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(
            nullable=False,
        )
    )
    athletes_start_interval: Mapped[Optional[int]] = mapped_column(
        Integer,
        nullable=False,
    )
    scoring_rule_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(
            nullable=False,
        )
    )

    athletes: Mapped[List["Athlete"]] = relationship("Athlete", back_populates="race")
    course_elements: Mapped[List["CourseElement"]] = relationship(
        "CourseElement", back_populates="race"
    )
