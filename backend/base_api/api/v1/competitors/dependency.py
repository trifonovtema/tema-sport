from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import Competitor
from core.schemas.competitor import CreateCompetitor, UpdateCompetitor, ReadCompetitor, FilterCompetitor


class CompetitorRepository(BaseRepository[Competitor, CreateCompetitor, UpdateCompetitor, FilterCompetitor]):
    pass


class CompetitorManager(BaseManager[CompetitorRepository, ReadCompetitor, FilterCompetitor]):
    pass


class CompetitorService(BaseService[CompetitorManager, ReadCompetitor, FilterCompetitor]):
    pass


get_competitor_repo, get_competitor_manager, get_competitor_service = create_dependency_factory(
    repo_class=CompetitorRepository,
    manager_class=CompetitorManager,
    service_class=CompetitorService,
    model=Competitor,
    create_schema=CreateCompetitor,
    update_schema=UpdateCompetitor,
    read_schema=ReadCompetitor,
    filter_schema=FilterCompetitor,
)
