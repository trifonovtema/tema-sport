from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import Competition
from core.schemas.competition import CreateCompetition, UpdateCompetition, ReadCompetition, FilterCompetition


class CompetitionRepository(BaseRepository[Competition, CreateCompetition, UpdateCompetition, FilterCompetition]):
    pass


class CompetitionManager(BaseManager[CompetitionRepository, ReadCompetition, FilterCompetition]):
    pass


class CompetitionService(BaseService[CompetitionManager, ReadCompetition, FilterCompetition]):
    pass


get_competition_repo, get_competition_manager, get_competition_service = create_dependency_factory(
    repo_class=CompetitionRepository,
    manager_class=CompetitionManager,
    service_class=CompetitionService,
    model=Competition,
    create_schema=CreateCompetition,
    update_schema=UpdateCompetition,
    read_schema=ReadCompetition,
    filter_schema=FilterCompetition,
)
