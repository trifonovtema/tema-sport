import uuid
from datetime import datetime, timezone
from fastapi_users_db_sqlalchemy.generics import GUID, TIMESTAMPAware, now_utc

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import func, TIMESTAMP

# from sqlalchemy import text

from core.config import settings


# class IdPkMixin:
#     # id: Mapped[get_settings().db.id_type.id_type] = mapped_column(primary_key=True)
#     if get_settings().db.id_type.id_type == uuid.UUID:
#         id: Mapped[uuid.UUID] = mapped_column(
#             primary_key=True,
#             # server_default=text("gen_random_uuid()"),
#             default=uuid.uuid4,
#         )
#     elif get_settings().db.id_type.id_type == int:
#         id: Mapped[int] = mapped_column(primary_key=True)


class CreatedAtMixin:

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        default=lambda: datetime.now(timezone.utc),
    )
