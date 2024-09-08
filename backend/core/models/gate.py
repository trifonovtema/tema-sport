from core.types.enum_types import GateType
from .base import Base
from core.config import settings
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, Integer, String, Enum as SqlEnum


class GateElement(Base):
    __tablename__ = "gates"
    course_element_id: Mapped[settings.db.id_type_class.get_id_type()] = mapped_column(
        nullable=False,
    )
    gate_number: Mapped[int] = mapped_column(
        nullable=True,
    )
    gate_type: Mapped[GateType] = mapped_column(
        SqlEnum(
            GateType,
            name="course_element_type",
            schema="tema_sport",
            # native_enum=False,
            # values_callable=lambda x: [e.value for e in x],
        ),
        nullable=True,
    )
