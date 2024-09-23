from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseAggRaceResult(BaseModel):
    competitor_id: settings.db.id_type_class.get_id_type() | None
    run_time: Any | None
    total_penalty: Any | None
    total_time: Any | None
    race_id: settings.db.id_type_class.get_id_type() | None
    race_class_id: settings.db.id_type_class.get_id_type() | None


class ReadAggRaceResult(BaseAggRaceResult):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateAggRaceResult(BaseAggRaceResult):
    competitor_id: settings.db.id_type_class.get_id_type() | None
    run_time: Any | None
    total_penalty: Any | None
    total_time: Any | None
    race_id: settings.db.id_type_class.get_id_type() | None
    race_class_id: settings.db.id_type_class.get_id_type() | None


class CreateAggRaceResult(BaseAggRaceResult):
    pass


class FilterAggRaceResult(BaseAggRaceResult):
    competitor_id: settings.db.id_type_class.get_id_type() | None
    run_time: Any | None
    total_penalty: Any | None
    total_time: Any | None
    race_id: settings.db.id_type_class.get_id_type() | None
    race_class_id: settings.db.id_type_class.get_id_type() | None
