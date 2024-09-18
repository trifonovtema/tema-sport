from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseStartRun(BaseModel):
    start_id: Any | None
    competitor_run_id: Any | None
    start_time: datetime | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class ReadStartRun(BaseStartRun):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateStartRun(BaseStartRun):
    start_id: Any | None
    competitor_run_id: Any | None
    start_time: datetime | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class CreateStartRun(BaseStartRun):
    pass


class FilterStartRun(BaseStartRun):
    start_id: Any | None
    competitor_run_id: Any | None
    start_time: datetime | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None
