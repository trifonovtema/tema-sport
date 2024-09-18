from typing import Optional

from .base import Base
from core.config import settings
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, Uuid


class Competition(Base):
    name: Mapped[Optional[str]] = mapped_column(Text)
    scoring_rules_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(Uuid)
    )
