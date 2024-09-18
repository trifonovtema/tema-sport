from base_api.api.v1.agg_run_results.dependency import (
    AggRunResultService,
    get_agg_run_result_service,
)
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.agg_run_result import (
    CreateAggRunResult,
    UpdateAggRunResult,
    FilterAggRunResult,
)
from core.config import settings


router = create_crud_router_factory(
    service_class=AggRunResultService,
    create_schema=CreateAggRunResult,
    update_schema=UpdateAggRunResult,
    filter_schema=FilterAggRunResult,
    service_dependency=get_agg_run_result_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.agg_run_results,
    tags=["AggRunResults"],
)
