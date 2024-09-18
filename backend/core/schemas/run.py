from pydantic import BaseModel, ConfigDict
from datetime import datetime
from core.config import settings


class BaseRun(BaseModel):
    name: str | None


class ReadRun(BaseRun):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateRun(BaseRun):
    name: str | None = None


class CreateRun(BaseRun):
    pass


class FilterRun(BaseModel):
    name: str | None = None
