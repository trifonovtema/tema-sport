from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import RaceStage
from core.schemas.race_stage import (
    CreateRaceStage,
    UpdateRaceStage,
    ReadRaceStage,
    FilterRaceStage,
)


class RaceStageRepository(
    BaseRepository[RaceStage, CreateRaceStage, UpdateRaceStage, FilterRaceStage]
):
    pass


class RaceStageManager(
    BaseManager[RaceStageRepository, ReadRaceStage, FilterRaceStage]
):
    pass


class RaceStageService(BaseService[RaceStageManager, ReadRaceStage, FilterRaceStage]):
    pass


get_race_stage_repo, get_race_stage_manager, get_race_stage_service = (
    create_dependency_factory(
        repo_class=RaceStageRepository,
        manager_class=RaceStageManager,
        service_class=RaceStageService,
        model=RaceStage,
        create_schema=CreateRaceStage,
        update_schema=UpdateRaceStage,
        read_schema=ReadRaceStage,
        filter_schema=FilterRaceStage,
    )
)
