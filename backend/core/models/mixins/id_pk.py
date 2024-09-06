import uuid

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

# from sqlalchemy import text

from backend.core.config import settings


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


class IdPkMixin:
    """Миксин для динамического определения типа ID."""

    id: Mapped[settings.db.id_type_class.get_id_type()] = mapped_column(
        primary_key=True,
        default=(
            uuid.uuid4 if settings.db.id_type_class.get_id_type() == uuid.UUID else None
        ),
    )
