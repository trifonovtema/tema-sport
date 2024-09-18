from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import LinkFinishCompetitorRun
from core.schemas.finish_run import (
    CreateFinishRun,
    UpdateFinishRun,
    ReadFinishRun,
    FilterFinishRun,
)


class FinishRunRepository(
    BaseRepository[
        LinkFinishCompetitorRun, CreateFinishRun, UpdateFinishRun, FilterFinishRun
    ]
):
    pass


class FinishRunManager(
    BaseManager[FinishRunRepository, ReadFinishRun, FilterFinishRun]
):
    pass


class FinishRunService(BaseService[FinishRunManager, ReadFinishRun, FilterFinishRun]):
    pass


get_finish_run_repo, get_finish_run_manager, get_finish_run_service = (
    create_dependency_factory(
        repo_class=FinishRunRepository,
        manager_class=FinishRunManager,
        service_class=FinishRunService,
        model=LinkFinishCompetitorRun,
        create_schema=CreateFinishRun,
        update_schema=UpdateFinishRun,
        read_schema=ReadFinishRun,
        filter_schema=FilterFinishRun,
    )
)
