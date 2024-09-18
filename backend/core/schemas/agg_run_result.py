from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseAggRunResult(BaseModel):
    run_id: Any | None
    athlete_id: Any | None
    run_time: Any | None
    total_penalty: int | None
    total_time: Any | None


class ReadAggRunResult(BaseAggRunResult):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateAggRunResult(BaseAggRunResult):
    run_id: Any | None
    athlete_id: Any | None
    run_time: Any | None
    total_penalty: int | None
    total_time: Any | None


class CreateAggRunResult(BaseAggRunResult):
    pass


class FilterAggRunResult(BaseAggRunResult):
    run_id: Any | None
    athlete_id: Any | None
    run_time: Any | None
    total_penalty: int | None
    total_time: Any | None
