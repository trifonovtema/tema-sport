from base_api.api.v1.race_classes.dependency import (
    RaceClassService,
    get_race_class_service,
)
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.race_class import CreateRaceClass, UpdateRaceClass, FilterRaceClass
from core.config import settings


router = create_crud_router_factory(
    service_class=RaceClassService,
    create_schema=CreateRaceClass,
    update_schema=UpdateRaceClass,
    filter_schema=FilterRaceClass,
    service_dependency=get_race_class_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.race_classes,
    tags=["RaceClasses"],
)
