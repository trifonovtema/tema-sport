from pydantic import BaseModel, ConfigDict
from datetime import datetime
from core.config import settings


class BaseSplit(BaseModel):
    course_element_id: settings.db.id_type_class.get_id_type() | None


class ReadSplit(BaseSplit):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateSplit(BaseSplit):
    course_element_id: settings.db.id_type_class.get_id_type() | None


class CreateSplit(BaseSplit):
    pass


class FilterSplit(BaseSplit):
    course_element_id: settings.db.id_type_class.get_id_type() | None
