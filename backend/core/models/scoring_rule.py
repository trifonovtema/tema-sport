from typing import Optional

from core.models import BaseTable
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text


class ScoringRule(BaseTable):
    scoring_rule: Mapped[Optional[str]] = mapped_column(Text)
