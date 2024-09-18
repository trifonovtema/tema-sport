from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Any
from core.config import settings


class BaseScoringRule(BaseModel):
    scoring_rule: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class ReadScoringRule(BaseScoringRule):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateScoringRule(BaseScoringRule):
    scoring_rule: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None


class CreateScoringRule(BaseScoringRule):
    pass


class FilterScoringRule(BaseScoringRule):
    scoring_rule: Any | None
    id: Any | None
    created_at: Any | None
    updated_at: Any | None
