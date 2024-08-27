from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from backend.settings import get_settings


class IdPkMixin:
    id: Mapped[get_settings().db.id_type.id_type] = mapped_column(primary_key=True)
