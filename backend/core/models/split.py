from .base import Base
from core.config import settings
from sqlalchemy.orm import Mapped, mapped_column


class SplitElement(Base):
    __tablename__ = "splits"
    course_element_id: Mapped[settings.db.id_type_class.get_id_type()] = mapped_column(
        nullable=False,
    )
