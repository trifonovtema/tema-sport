from base_api.api.v1.finish_runs.dependency import (
    FinishRunService,
    get_finish_run_service,
)
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.finish_run import CreateFinishRun, UpdateFinishRun, FilterFinishRun
from core.config import settings


router = create_crud_router_factory(
    service_class=FinishRunService,
    create_schema=CreateFinishRun,
    update_schema=UpdateFinishRun,
    filter_schema=FilterFinishRun,
    service_dependency=get_finish_run_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.finish_runs,
    tags=["FinishRuns"],
)
