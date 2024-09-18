from typing import Optional, List, TYPE_CHECKING

from core.config import settings
from core.models.link_competition_registered_user import LinkCompetitionRegisteredUser
from core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

if TYPE_CHECKING:
    from core.models.course_element import CourseElement


class JudgementGroup(Base):
    competition_registered_user_id: Mapped[
        Optional[settings.db.id_type_class.get_id_type()]
    ] = mapped_column(
        ForeignKey(LinkCompetitionRegisteredUser.id),
        nullable=True,
    )

    course_elements: Mapped[List["CourseElement"]] = relationship(
        "CourseElement", back_populates="judgement_group"
    )
