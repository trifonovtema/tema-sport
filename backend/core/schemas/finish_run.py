from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseFinishRun(BaseModel):
    finish_id: Any | None
    competitor_run_id: Any | None
    finish_time: datetime | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class ReadFinishRun(BaseFinishRun):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateFinishRun(BaseFinishRun):
    finish_id: Any | None
    competitor_run_id: Any | None
    finish_time: datetime | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class CreateFinishRun(BaseFinishRun):
    pass


class FilterFinishRun(BaseFinishRun):
    finish_id: Any | None
    competitor_run_id: Any | None
    finish_time: datetime | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None
