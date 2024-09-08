from pydantic import BaseModel, ConfigDict
from datetime import datetime
from core.config import settings
from core.types.enum_types import FinishType, GateType


class BaseFinish(BaseModel):
    course_element_id: settings.db.id_type_class.get_id_type() | None


class ReadFinish(BaseFinish):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateFinish(BaseFinish):
    course_element_id: settings.db.id_type_class.get_id_type() | None


class CreateFinish(BaseFinish):
    pass


class FilterFinish(BaseFinish):
    course_element_id: settings.db.id_type_class.get_id_type() | None
