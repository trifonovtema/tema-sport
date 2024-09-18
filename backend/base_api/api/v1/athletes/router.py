from base_api.api.v1.athletes.dependency import AthleteService, get_athlete_service
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.athlete import CreateAthlete, UpdateAthlete, FilterAthlete
from core.config import settings


router = create_crud_router_factory(
    service_class=AthleteService,
    create_schema=CreateAthlete,
    update_schema=UpdateAthlete,
    filter_schema=FilterAthlete,
    service_dependency=get_athlete_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.athletes,
    tags=["Athletes"],
)
