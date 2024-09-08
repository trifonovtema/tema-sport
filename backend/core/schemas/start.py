from pydantic import BaseModel, ConfigDict
from datetime import datetime
from core.config import settings
from core.types.enum_types import GateType


class BaseStart(BaseModel):
    course_element_id: settings.db.id_type_class.get_id_type() | None


class ReadStart(BaseStart):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateStart(BaseStart):
    course_element_id: settings.db.id_type_class.get_id_type() | None


class CreateStart(BaseStart):
    pass


class FilterStart(BaseStart):
    course_element_id: settings.db.id_type_class.get_id_type() | None
