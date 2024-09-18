from typing import Optional

from core.config import settings
from core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text


class MedalGroup(Base):
    group_name: Mapped[Optional[str]] = mapped_column(Text)
    group_type: Mapped[Optional[str]] = mapped_column(Text)
    competition_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(nullable=True)
    )
