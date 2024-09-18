from typing import Optional

from core.config import settings
from core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger


class AggRaceResult(Base):
    competitor_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]]
    run_time: Mapped[Optional[int]] = mapped_column(BigInteger)
    total_penalty: Mapped[Optional[int]] = mapped_column(BigInteger)
    total_time: Mapped[Optional[int]] = mapped_column(BigInteger)
    race_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]]
    race_class_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]]
