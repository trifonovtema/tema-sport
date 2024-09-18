from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseCompetitionScoringRule(BaseModel):
    competition_id: Any | None
    calculated_by_rule: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class ReadCompetitionScoringRule(BaseCompetitionScoringRule):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateCompetitionScoringRule(BaseCompetitionScoringRule):
    competition_id: Any | None
    calculated_by_rule: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class CreateCompetitionScoringRule(BaseCompetitionScoringRule):
    pass


class FilterCompetitionScoringRule(BaseCompetitionScoringRule):
    competition_id: Any | None
    calculated_by_rule: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None
