from base_api.api.v1.race_stages.dependency import (
    RaceStageService,
    get_race_stage_service,
)
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.race_stage import CreateRaceStage, UpdateRaceStage, FilterRaceStage
from core.config import settings


router = create_crud_router_factory(
    service_class=RaceStageService,
    create_schema=CreateRaceStage,
    update_schema=UpdateRaceStage,
    filter_schema=FilterRaceStage,
    service_dependency=get_race_stage_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.race_stages,
    tags=["RaceStages"],
)
