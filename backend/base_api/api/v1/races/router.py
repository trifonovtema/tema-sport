from base_api.api.v1.races.dependency import RaceService, get_race_service
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.race import CreateRace, UpdateRace, FilterRace
from core.config import settings


router = create_crud_router_factory(
    service_class=RaceService,
    create_schema=CreateRace,
    update_schema=UpdateRace,
    filter_schema=FilterRace,
    service_dependency=get_race_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.races,
    tags=["Races"],
)
