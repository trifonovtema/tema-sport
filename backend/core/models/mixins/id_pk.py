import uuid

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import text

from backend.settings import get_settings


class IdPkMixin:
    # id: Mapped[get_settings().db.id_type.id_type] = mapped_column(primary_key=True)
    if get_settings().db.id_type.id_type == uuid.UUID:
        id: Mapped[uuid.UUID] = mapped_column(
            primary_key=True,
            server_default=text("gen_random_uuid()"),
        )
    elif get_settings().db.id_type.id_type == int:
        id: Mapped[int] = mapped_column(primary_key=True)
