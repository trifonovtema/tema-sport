from datetime import datetime
from typing import TYPE_CHECKING

from .base import Base
from .mixins.created_at import CreatedAtMixin
from core.config import settings
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Run(Base):
    if TYPE_CHECKING:  # pragma: no cover
        id: settings.db.id_type_class.get_id_type()
        user_id: settings.db.id_type_class.get_id_type() | None
        race_id: settings.db.id_type_class.get_id_type() | None
        name: str | None
    #     scheduled_time: datetime | None
    else:
        name: Mapped[str] = mapped_column(index=True, nullable=False)
        user_id: Mapped[settings.db.id_type_class.get_id_type()]
        race_id: Mapped[settings.db.id_type_class.get_id_type()]
        # scheduled_time: Mapped[datetime]
