from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import Athlete
from core.schemas.athlete import CreateAthlete, UpdateAthlete, ReadAthlete, FilterAthlete


class AthleteRepository(BaseRepository[Athlete, CreateAthlete, UpdateAthlete, FilterAthlete]):
    pass


class AthleteManager(BaseManager[AthleteRepository, ReadAthlete, FilterAthlete]):
    pass


class AthleteService(BaseService[AthleteManager, ReadAthlete, FilterAthlete]):
    pass


get_athlete_repo, get_athlete_manager, get_athlete_service = create_dependency_factory(
    repo_class=AthleteRepository,
    manager_class=AthleteManager,
    service_class=AthleteService,
    model=Athlete,
    create_schema=CreateAthlete,
    update_schema=UpdateAthlete,
    read_schema=ReadAthlete,
    filter_schema=FilterAthlete,
)
