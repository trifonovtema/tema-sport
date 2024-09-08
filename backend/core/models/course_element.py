from sqlalchemy import Column, Integer, String, Enum as SqlEnum, ForeignKey
from sqlalchemy.orm import relationship

from core.config import settings
from core.models import Base, Race
from core.types.enum_types import CourseElementType, GateType
from datetime import datetime
from typing import TYPE_CHECKING

from .base import Base
from core.config import settings
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import TIMESTAMP


class CourseElement(Base):
    __tablename__ = "course_elements"
    race_id: Mapped[settings.db.id_type_class.get_id_type()] = mapped_column(
        nullable=True,
    )
    number: Mapped[int] = mapped_column(
        nullable=True,
    )
    type: Mapped[CourseElementType] = mapped_column(
        SqlEnum(
            CourseElementType,
            name="course_element_type",
            schema="tema_sport",
            # native_enum=False,
            # values_callable=lambda x: [e.value for e in x],
        ),
        nullable=True,
    )
