from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import AggRunResult
from core.schemas.agg_run_result import (
    CreateAggRunResult,
    UpdateAggRunResult,
    ReadAggRunResult,
    FilterAggRunResult,
)


class AggRunResultRepository(
    BaseRepository[
        AggRunResult, CreateAggRunResult, UpdateAggRunResult, FilterAggRunResult
    ]
):
    pass


class AggRunResultManager(
    BaseManager[AggRunResultRepository, ReadAggRunResult, FilterAggRunResult]
):
    pass


class AggRunResultService(
    BaseService[AggRunResultManager, ReadAggRunResult, FilterAggRunResult]
):
    pass


get_agg_run_result_repo, get_agg_run_result_manager, get_agg_run_result_service = (
    create_dependency_factory(
        repo_class=AggRunResultRepository,
        manager_class=AggRunResultManager,
        service_class=AggRunResultService,
        model=AggRunResult,
        create_schema=CreateAggRunResult,
        update_schema=UpdateAggRunResult,
        read_schema=ReadAggRunResult,
        filter_schema=FilterAggRunResult,
    )
)
