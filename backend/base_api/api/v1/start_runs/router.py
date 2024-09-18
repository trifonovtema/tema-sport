from base_api.api.v1.start_runs.dependency import StartRunService, get_start_run_service
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.start_run import CreateStartRun, UpdateStartRun, FilterStartRun
from core.config import settings


router = create_crud_router_factory(
    service_class=StartRunService,
    create_schema=CreateStartRun,
    update_schema=UpdateStartRun,
    filter_schema=FilterStartRun,
    service_dependency=get_start_run_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.start_runs,
    tags=["StartRuns"],
)
