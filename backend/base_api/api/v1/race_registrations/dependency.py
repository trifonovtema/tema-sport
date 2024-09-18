from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import RaceRegistration
from core.schemas.race_registration import (
    CreateRaceRegistration,
    UpdateRaceRegistration,
    ReadRaceRegistration,
    FilterRaceRegistration,
)


class RaceRegistrationRepository(
    BaseRepository[
        RaceRegistration,
        CreateRaceRegistration,
        UpdateRaceRegistration,
        FilterRaceRegistration,
    ]
):
    pass


class RaceRegistrationManager(
    BaseManager[
        RaceRegistrationRepository, ReadRaceRegistration, FilterRaceRegistration
    ]
):
    pass


class RaceRegistrationService(
    BaseService[RaceRegistrationManager, ReadRaceRegistration, FilterRaceRegistration]
):
    pass


(
    get_raceregistration_repo,
    get_raceregistration_manager,
    get_raceregistration_service,
) = create_dependency_factory(
    repo_class=RaceRegistrationRepository,
    manager_class=RaceRegistrationManager,
    service_class=RaceRegistrationService,
    model=RaceRegistration,
    create_schema=CreateRaceRegistration,
    update_schema=UpdateRaceRegistration,
    read_schema=ReadRaceRegistration,
    filter_schema=FilterRaceRegistration,
)
