from sqlalchemy import (
    Integer,
    Enum as SqlEnum,
    Uuid,
)
from sqlalchemy.orm import relationship

from core.models.race import Race
from core.types.enum_types import CourseElementType
from typing import Optional

from .base import Base
from core.config import settings
from sqlalchemy.orm import Mapped, mapped_column

from .judgement_group import JudgementGroup


# class CourseElement(BaseTable):
#     __tablename__ = "course_elements"
#     race_id: Mapped[settings.db.id_type_class.get_id_type()] = mapped_column(
#         nullable=True,
#     )
#     number: Mapped[int] = mapped_column(
#         nullable=True,
#     )
#     type: # Mapped[CourseElementType] = mapped_column(
#         SqlEnum(
#             CourseElementType,
#             name="course_element_type",
#             schema="tema_sport",
#             # native_enum=False,
#             # values_callable=lambda x: [e.value for e in x],
#         ),
#         nullable=True,
#     )


class CourseElement(Base):
    # __table_args__ = (
    #     ForeignKeyConstraint(
    #         ["judgement_group_id"],
    #         ["tema_sport.judjement_groups.id"],
    #         name="fk_course_elements_judjement_groups",
    #     ),
    #     ForeignKeyConstraint(
    #         ["race_id"], ["tema_sport.races.id"], name="fk_course_elements_races"
    #     ),
    #     PrimaryKeyConstraint("id", name="pk_course_elements"),
    #     {"schema": "tema_sport"},
    # )

    race_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = mapped_column(
        Uuid, nullable=True
    )
    number: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    type: Mapped[Optional[str]] = mapped_column(
        SqlEnum(
            CourseElementType,
            name="course_element_type",
            schema=settings.db.SCHEMA,
            # native_enum=False,
            # values_callable=lambda x: [e.value for e in x],
        ),
        nullable=True,
    )
    judgement_group_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(nullable=True)
    )

    judgement_group: Mapped["JudgementGroup"] = relationship(
        "JudgementGroup", back_populates="course_elements"
    )
    race: Mapped["Race"] = relationship("Race", back_populates="course_elements")
