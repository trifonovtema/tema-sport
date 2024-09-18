from base_api.api.v1.competitions.dependency import CompetitionService, get_competition_service
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.competition import CreateCompetition, UpdateCompetition, FilterCompetition
from core.config import settings


router = create_crud_router_factory(
    service_class=CompetitionService,
    create_schema=CreateCompetition,
    update_schema=UpdateCompetition,
    filter_schema=FilterCompetition,
    service_dependency=get_competition_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.competitions,
    tags=["Competitions"],
)
