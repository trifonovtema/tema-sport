from typing import Optional

from core.config import settings
from core.models import BaseTable
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer


class CompetitionResult(BaseTable):
    competition_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(nullable=True)
    )
    competitor_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(nullable=True)
    )
    run_time: Mapped[Optional[int]] = mapped_column(Integer)
    total_penalty: Mapped[Optional[int]] = mapped_column(Integer)
    total_time: Mapped[Optional[int]] = mapped_column(Integer)
