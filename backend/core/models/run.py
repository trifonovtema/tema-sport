import uuid
from datetime import datetime

from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import TIMESTAMP, String, Uuid
from sqlalchemy.orm import relationship
from typing import List, Optional, TYPE_CHECKING


if TYPE_CHECKING:
    from .competitor_run import CompetitorRun


# class Run(BaseTable):
#     if TYPE_CHECKING:  # pragma: no cover
#         id: settings.db.id_type_class.get_id_type()
#         user_id: settings.db.id_type_class.get_id_type() | None
#         race_id: settings.db.id_type_class.get_id_type() | None
#         name: str | None
#         scheduled_time: datetime | None
#     else:
#         name: Mapped[str] = mapped_column(
#             index=True,
#             nullable=False,
#         )
#         user_id: Mapped[settings.db.id_type_class.get_id_type()] = mapped_column(
#             nullable=True,
#         )
#         race_id: Mapped[settings.db.id_type_class.get_id_type()] = mapped_column(
#             nullable=True,
#         )
#         scheduled_time: Mapped[datetime] = mapped_column(
#             TIMESTAMP(timezone=True),
#             nullable=True,
#         )


class Run(Base):

    name: Mapped[str] = mapped_column(String)

    race_stage_id: Mapped[Optional[uuid.UUID]] = mapped_column(Uuid)
    scheduled_timestamp: Mapped[Optional[datetime]] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=True,
    )

    competitor_runs: Mapped[List["CompetitorRun"]] = relationship(
        "CompetitorRun", back_populates="run"
    )
