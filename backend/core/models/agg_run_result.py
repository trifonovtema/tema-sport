from typing import Optional

from core.config import settings
from core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, Integer


class AggRunResult(Base):
    run_id: Mapped[settings.db.id_type_class.get_id_type()] = mapped_column(
        nullable=True
    )
    athlete_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(nullable=True)
    )
    run_time: Mapped[Optional[int]] = mapped_column(BigInteger)
    total_penalty: Mapped[Optional[int]] = mapped_column(Integer)
    total_time: Mapped[Optional[int]] = mapped_column(BigInteger)
