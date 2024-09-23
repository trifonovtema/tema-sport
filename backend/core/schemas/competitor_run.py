from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseCompetitorRun(BaseModel):
    competitor_id: settings.db.id_type_class.get_id_type() | None
    scheduled_time: datetime | None
    run_id: settings.db.id_type_class.get_id_type() | None


class ReadCompetitorRun(BaseCompetitorRun):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateCompetitorRun(BaseCompetitorRun):
    competitor_id: settings.db.id_type_class.get_id_type() | None
    scheduled_time: datetime | None
    run_id: settings.db.id_type_class.get_id_type() | None


class CreateCompetitorRun(BaseCompetitorRun):
    pass


class FilterCompetitorRun(BaseCompetitorRun):
    competitor_id: settings.db.id_type_class.get_id_type() | None
    scheduled_time: datetime | None
    run_id: settings.db.id_type_class.get_id_type() | None
