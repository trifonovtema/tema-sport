from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseRaceStage(BaseModel):
    race_class_id: Any | None
    runs_number: int | None
    athletes_start_interval: int | None
    parent_race_stage_id: Any | None
    type: Any | None
    scoring_rule_id: Any | None
    athletes_qualified_count: int | None
    athletes_qualified_percentage: int | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class ReadRaceStage(BaseRaceStage):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateRaceStage(BaseRaceStage):
    race_class_id: Any | None
    runs_number: int | None
    athletes_start_interval: int | None
    parent_race_stage_id: Any | None
    type: Any | None
    scoring_rule_id: Any | None
    athletes_qualified_count: int | None
    athletes_qualified_percentage: int | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class CreateRaceStage(BaseRaceStage):
    pass


class FilterRaceStage(BaseRaceStage):
    race_class_id: Any | None
    runs_number: int | None
    athletes_start_interval: int | None
    parent_race_stage_id: Any | None
    type: Any | None
    scoring_rule_id: Any | None
    athletes_qualified_count: int | None
    athletes_qualified_percentage: int | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None
