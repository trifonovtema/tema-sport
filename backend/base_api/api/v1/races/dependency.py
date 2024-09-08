from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import Race
from core.schemas.race import CreateRace, UpdateRace, ReadRace, FilterRace


class RaceRepository(BaseRepository[Race, CreateRace, UpdateRace, FilterRace]):
    pass


class RaceManager(BaseManager[RaceRepository, ReadRace, FilterRace]):
    pass


class RaceService(BaseService[RaceManager, ReadRace, FilterRace]):
    pass


get_race_repo, get_race_manager, get_race_service = create_dependency_factory(
    repo_class=RaceRepository,
    manager_class=RaceManager,
    service_class=RaceService,
    model=Race,
    create_schema=CreateRace,
    update_schema=UpdateRace,
    read_schema=ReadRace,
    filter_schema=FilterRace,
)
