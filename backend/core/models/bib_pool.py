from typing import Optional

from core.config import settings
from core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, ForeignKey

from core.models.competition import Competition


class BibPool(Base):
    bib_number: Mapped[Optional[int]] = mapped_column(Integer)
    is_exists: Mapped[bool] = mapped_column(
        default=True,
        nullable=False,
    )
    competition_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(
            ForeignKey(Competition.id),
            nullable=False,
        )
    )
