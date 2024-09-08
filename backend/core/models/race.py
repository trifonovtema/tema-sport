from typing import TYPE_CHECKING
from .base import Base
from core.config import settings
from sqlalchemy.orm import Mapped, mapped_column


class Race(Base):
    if TYPE_CHECKING:  # pragma: no cover
        id: settings.db.id_type_class.get_id_type()
        competition_id: settings.db.id_type_class.get_id_type() | None
        name: str | None
    else:
        name: Mapped[str] = mapped_column(
            index=True,
            nullable=False,
        )
        competition_id: Mapped[settings.db.id_type_class.get_id_type()] = mapped_column(
            nullable=True,
        )
