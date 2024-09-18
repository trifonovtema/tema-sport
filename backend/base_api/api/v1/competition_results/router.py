from base_api.api.v1.competition_results.dependency import (
    CompetitionResultService,
    get_competition_result_service,
)
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.competition_result import (
    CreateCompetitionResult,
    UpdateCompetitionResult,
    FilterCompetitionResult,
)
from core.config import settings


router = create_crud_router_factory(
    service_class=CompetitionResultService,
    create_schema=CreateCompetitionResult,
    update_schema=UpdateCompetitionResult,
    filter_schema=FilterCompetitionResult,
    service_dependency=get_competition_result_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.competition_results,
    tags=["CompetitionResults"],
)
