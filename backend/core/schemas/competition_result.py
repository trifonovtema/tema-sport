from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseCompetitionResult(BaseModel):
    competition_id: settings.db.id_type_class.get_id_type() | None
    competitor_id: settings.db.id_type_class.get_id_type() | None
    run_time: int | None
    total_penalty: int | None
    total_time: int | None


class ReadCompetitionResult(BaseCompetitionResult):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateCompetitionResult(BaseCompetitionResult):
    competition_id: settings.db.id_type_class.get_id_type() | None
    competitor_id: settings.db.id_type_class.get_id_type() | None
    run_time: int | None
    total_penalty: int | None
    total_time: int | None


class CreateCompetitionResult(BaseCompetitionResult):
    pass


class FilterCompetitionResult(BaseCompetitionResult):
    competition_id: settings.db.id_type_class.get_id_type() | None
    competitor_id: settings.db.id_type_class.get_id_type() | None
    run_time: int | None
    total_penalty: int | None
    total_time: int | None
