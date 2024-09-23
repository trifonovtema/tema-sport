from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseGateRun(BaseModel):
    gate_id: settings.db.id_type_class.get_id_type() | None
    competitor_run_id: settings.db.id_type_class.get_id_type() | None
    penalty: int | None
    athlete_id: settings.db.id_type_class.get_id_type() | None


class ReadGateRun(BaseGateRun):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateGateRun(BaseGateRun):
    gate_id: settings.db.id_type_class.get_id_type() | None
    competitor_run_id: settings.db.id_type_class.get_id_type() | None
    penalty: int | None
    athlete_id: settings.db.id_type_class.get_id_type() | None


class CreateGateRun(BaseGateRun):
    pass


class FilterGateRun(BaseGateRun):
    gate_id: settings.db.id_type_class.get_id_type() | None
    competitor_run_id: settings.db.id_type_class.get_id_type() | None
    penalty: int | None
    athlete_id: settings.db.id_type_class.get_id_type() | None
