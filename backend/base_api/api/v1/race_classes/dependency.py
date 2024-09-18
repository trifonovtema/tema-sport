from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import RaceClass
from core.schemas.race_class import (
    CreateRaceClass,
    UpdateRaceClass,
    ReadRaceClass,
    FilterRaceClass,
)


class RaceClassRepository(
    BaseRepository[RaceClass, CreateRaceClass, UpdateRaceClass, FilterRaceClass]
):
    pass


class RaceClassManager(
    BaseManager[RaceClassRepository, ReadRaceClass, FilterRaceClass]
):
    pass


class RaceClassService(BaseService[RaceClassManager, ReadRaceClass, FilterRaceClass]):
    pass


get_race_class_repo, get_race_class_manager, get_race_class_service = (
    create_dependency_factory(
        repo_class=RaceClassRepository,
        manager_class=RaceClassManager,
        service_class=RaceClassService,
        model=RaceClass,
        create_schema=CreateRaceClass,
        update_schema=UpdateRaceClass,
        read_schema=ReadRaceClass,
        filter_schema=FilterRaceClass,
    )
)
