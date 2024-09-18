from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import LinkStartCompetitorRun
from core.schemas.start_run import (
    CreateStartRun,
    UpdateStartRun,
    ReadStartRun,
    FilterStartRun,
)


class StartRunRepository(
    BaseRepository[
        LinkStartCompetitorRun, CreateStartRun, UpdateStartRun, FilterStartRun
    ]
):
    pass


class StartRunManager(BaseManager[StartRunRepository, ReadStartRun, FilterStartRun]):
    pass


class StartRunService(BaseService[StartRunManager, ReadStartRun, FilterStartRun]):
    pass


get_start_run_repo, get_start_run_manager, get_start_run_service = (
    create_dependency_factory(
        repo_class=StartRunRepository,
        manager_class=StartRunManager,
        service_class=StartRunService,
        model=LinkStartCompetitorRun,
        create_schema=CreateStartRun,
        update_schema=UpdateStartRun,
        read_schema=ReadStartRun,
        filter_schema=FilterStartRun,
    )
)
