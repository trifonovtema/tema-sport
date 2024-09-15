from typing import Optional

from core.models import BaseTable
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer


class Bib(BaseTable):
    bib_number: Mapped[Optional[int]] = mapped_column(Integer)
