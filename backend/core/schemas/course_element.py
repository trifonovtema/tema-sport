from pydantic import BaseModel, ConfigDict
from datetime import datetime
from core.config import settings
from core.types.enum_types import CourseElementType


class BaseCourseElement(BaseModel):
    race_id: settings.db.id_type_class.get_id_type() | None
    number: int | None
    type: CourseElementType | None


class ReadCourseElement(BaseCourseElement):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateCourseElement(BaseCourseElement):
    number: int | None
    type: CourseElementType | None


class CreateCourseElement(BaseCourseElement):
    pass


class FilterCourseElement(BaseCourseElement):
    number: int | None
    type: CourseElementType | None
