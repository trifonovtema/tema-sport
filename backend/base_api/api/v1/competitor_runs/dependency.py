from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import CompetitorRun
from core.schemas.competitor_run import (
    CreateCompetitorRun,
    UpdateCompetitorRun,
    ReadCompetitorRun,
    FilterCompetitorRun,
)


class CompetitorRunRepository(
    BaseRepository[
        CompetitorRun, CreateCompetitorRun, UpdateCompetitorRun, FilterCompetitorRun
    ]
):
    pass


class CompetitorRunManager(
    BaseManager[CompetitorRunRepository, ReadCompetitorRun, FilterCompetitorRun]
):
    pass


class CompetitorRunService(
    BaseService[CompetitorRunManager, ReadCompetitorRun, FilterCompetitorRun]
):
    pass


get_competitor_run_repo, get_competitor_run_manager, get_competitor_run_service = (
    create_dependency_factory(
        repo_class=CompetitorRunRepository,
        manager_class=CompetitorRunManager,
        service_class=CompetitorRunService,
        model=CompetitorRun,
        create_schema=CreateCompetitorRun,
        update_schema=UpdateCompetitorRun,
        read_schema=ReadCompetitorRun,
        filter_schema=FilterCompetitorRun,
    )
)
