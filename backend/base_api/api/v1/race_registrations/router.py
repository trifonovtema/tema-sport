from base_api.api.v1.race_registrations.dependency import (
    RaceRegistrationService,
    get_raceregistration_service,
)
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.race_registration import (
    CreateRaceRegistration,
    UpdateRaceRegistration,
    FilterRaceRegistration,
)
from core.config import settings


router = create_crud_router_factory(
    service_class=RaceRegistrationService,
    create_schema=CreateRaceRegistration,
    update_schema=UpdateRaceRegistration,
    filter_schema=FilterRaceRegistration,
    service_dependency=get_raceregistration_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.race_registrations,
    tags=["RaceRegistrations"],
)
