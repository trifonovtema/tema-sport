from core.types.enum_types import GateType
from .base import Base
from core.config import settings
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as SqlEnum


class Gate(Base):
    course_element_id: Mapped[settings.db.id_type_class.get_id_type()] = mapped_column(
        nullable=False,
    )
    number: Mapped[int] = mapped_column(
        nullable=True,
    )
    type: Mapped[GateType] = mapped_column(
        SqlEnum(
            GateType,
            name="gate_type",
            schema=settings.db.SCHEMA,
            # native_enum=False,
            # values_callable=lambda x: [e.value for e in x],
        ),
        nullable=True,
    )
