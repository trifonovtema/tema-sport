from typing import TYPE_CHECKING

from .base import Base
from core.config import settings
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Competition(Base):
    if TYPE_CHECKING:  # pragma: no cover
        id: settings.db.id_type_class.get_id_type()
        name: str
    else:
        name: Mapped[str] = mapped_column(
            String(length=4000), unique=True, index=True, nullable=False
        )
