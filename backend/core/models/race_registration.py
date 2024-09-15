from typing import Optional

from core.config import settings
from core.models import BaseTable
from sqlalchemy.orm import Mapped, mapped_column


class RaceRegistration(BaseTable):
    race_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = mapped_column(
        nullable=True
    )
    competitor_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(nullable=True)
    )
    race_class_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(nullable=True)
    )
