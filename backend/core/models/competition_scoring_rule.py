from typing import Optional

from core.config import settings
from core.models import BaseTable
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text


class CompetitionScoringRule(BaseTable):
    competition_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(nullable=True)
    )
    calculated_by_rule: Mapped[Optional[str]] = mapped_column(Text)
