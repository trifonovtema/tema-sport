from base_api.api.v1.competitors.dependency import CompetitorService, get_competitor_service
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.competitor import CreateCompetitor, UpdateCompetitor, FilterCompetitor
from core.config import settings


router = create_crud_router_factory(
    service_class=CompetitorService,
    create_schema=CreateCompetitor,
    update_schema=UpdateCompetitor,
    filter_schema=FilterCompetitor,
    service_dependency=get_competitor_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.competitors,
    tags=["Competitors"],
)
