from pydantic import BaseModel, ConfigDict
from datetime import datetime
from core.config import settings
from core.types.enum_types import CourseElementType, GateType


class BaseGate(BaseModel):
    course_element_id: settings.db.id_type_class.get_id_type() | None
    gate_number: int | None
    gate_type: GateType | None


class ReadGate(BaseGate):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateGate(BaseGate):
    course_element_id: settings.db.id_type_class.get_id_type() | None
    gate_number: int | None
    gate_type: GateType | None


class CreateGate(BaseGate):
    pass


class FilterGate(BaseGate):
    course_element_id: settings.db.id_type_class.get_id_type() | None
    gate_number: int | None
    gate_type: GateType | None
