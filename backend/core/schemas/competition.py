from pydantic import BaseModel, ConfigDict
from datetime import datetime
from core.config import settings


class BaseCompetition(BaseModel):
    name: str | None


class ReadCompetition(BaseCompetition):
    id: settings.db.id_type_class.get_id_type()
    created_at: datetime | None
    updated_at: datetime | None
    model_config = ConfigDict(from_attributes=True)


class UpdateCompetition(BaseCompetition):
    pass


class CreateCompetition(BaseCompetition):
    pass


class FilterCompetition(BaseCompetition):
    pass
