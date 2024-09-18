from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import AggRaceResult
from core.schemas.agg_race_result import (
    CreateAggRaceResult,
    UpdateAggRaceResult,
    ReadAggRaceResult,
    FilterAggRaceResult,
)


class AggRaceResultRepository(
    BaseRepository[
        AggRaceResult, CreateAggRaceResult, UpdateAggRaceResult, FilterAggRaceResult
    ]
):
    pass


class AggRaceResultManager(
    BaseManager[AggRaceResultRepository, ReadAggRaceResult, FilterAggRaceResult]
):
    pass


class AggRaceResultService(
    BaseService[AggRaceResultManager, ReadAggRaceResult, FilterAggRaceResult]
):
    pass


get_agg_race_result_repo, get_agg_race_result_manager, get_agg_race_result_service = (
    create_dependency_factory(
        repo_class=AggRaceResultRepository,
        manager_class=AggRaceResultManager,
        service_class=AggRaceResultService,
        model=AggRaceResult,
        create_schema=CreateAggRaceResult,
        update_schema=UpdateAggRaceResult,
        read_schema=ReadAggRaceResult,
        filter_schema=FilterAggRaceResult,
    )
)
