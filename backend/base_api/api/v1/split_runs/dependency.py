from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import LinkSplitCompetitorRun
from core.schemas.split_run import (
    CreateSplitRun,
    UpdateSplitRun,
    ReadSplitRun,
    FilterSplitRun,
)


class SplitRunRepository(
    BaseRepository[
        LinkSplitCompetitorRun, CreateSplitRun, UpdateSplitRun, FilterSplitRun
    ]
):
    pass


class SplitRunManager(BaseManager[SplitRunRepository, ReadSplitRun, FilterSplitRun]):
    pass


class SplitRunService(BaseService[SplitRunManager, ReadSplitRun, FilterSplitRun]):
    pass


get_split_run_repo, get_split_run_manager, get_split_run_service = (
    create_dependency_factory(
        repo_class=SplitRunRepository,
        manager_class=SplitRunManager,
        service_class=SplitRunService,
        model=LinkSplitCompetitorRun,
        create_schema=CreateSplitRun,
        update_schema=UpdateSplitRun,
        read_schema=ReadSplitRun,
        filter_schema=FilterSplitRun,
    )
)
