from typing import Optional

from .basetable import BaseTable
from core.config import settings
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, Uuid


class Competition(BaseTable):
    name: Mapped[Optional[str]] = mapped_column(Text)
    scoring_rules_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(Uuid)
    )
