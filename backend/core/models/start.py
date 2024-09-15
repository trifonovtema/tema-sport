from .basetable import BaseTable
from core.config import settings
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Uuid


class Start(BaseTable):
    course_element_id: Mapped[settings.db.id_type_class.get_id_type()] = mapped_column(
        Uuid,
        nullable=False,
    )
