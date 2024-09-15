from typing import Optional

from .basetable import BaseTable
from core.config import settings
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer


# class Split(BaseTable):
#     __tablename__ = "splits"
#     course_element_id: Mapped[settings.db.id_type_class.get_id_type()] = mapped_column(
#         nullable=False,
#     )


class Split(BaseTable):

    course_element_id: Mapped[Optional[settings.db.id_type_class.get_id_type()]] = (
        mapped_column(
            nullable=False,
        )
    )
    number: Mapped[Optional[int]] = mapped_column(Integer)
