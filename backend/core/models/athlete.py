from typing import Optional

from core.config import settings
from core.models.base import Base
from core.models.race import Race
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Uuid


class Athlete(Base):
    competition_registered_user_id: Mapped[
        Optional[settings.db.id_type_class.get_id_type()]
    ] = mapped_column(Uuid)
    race_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = mapped_column(
        Uuid
    )

    race: Mapped["Race"] = relationship("Race", back_populates="athletes")
