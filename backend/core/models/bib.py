from typing import Optional

from core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer


class Bib(Base):
    bib_number: Mapped[Optional[int]] = mapped_column(Integer)
