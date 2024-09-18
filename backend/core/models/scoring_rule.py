from typing import Optional

from core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text


class ScoringRule(Base):
    scoring_rule: Mapped[Optional[str]] = mapped_column(Text)
