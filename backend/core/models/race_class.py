from typing import Optional

from core.config import settings
from core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer


class RaceClass(Base):
    __tablename__ = "race_classes"

    name: Mapped[Optional[int]] = mapped_column(Integer)
    athletes_qualified_count: Mapped[Optional[int]] = mapped_column(Integer)
    athletes_qualified_percentage: Mapped[Optional[int]] = mapped_column(Integer)
    race_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = mapped_column(
        nullable=True
    )
