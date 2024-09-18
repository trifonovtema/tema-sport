from base_api.api.v1.agg_race_results.dependency import (
    AggRaceResultService,
    get_agg_race_result_service,
)
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.agg_race_result import (
    CreateAggRaceResult,
    UpdateAggRaceResult,
    FilterAggRaceResult,
)
from core.config import settings


router = create_crud_router_factory(
    service_class=AggRaceResultService,
    create_schema=CreateAggRaceResult,
    update_schema=UpdateAggRaceResult,
    filter_schema=FilterAggRaceResult,
    service_dependency=get_agg_race_result_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.agg_race_results,
    tags=["AggRaceResults"],
)
