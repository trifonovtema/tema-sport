from base_api.api.v1.split_runs.dependency import SplitRunService, get_split_run_service
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.split_run import CreateSplitRun, UpdateSplitRun, FilterSplitRun
from core.config import settings


router = create_crud_router_factory(
    service_class=SplitRunService,
    create_schema=CreateSplitRun,
    update_schema=UpdateSplitRun,
    filter_schema=FilterSplitRun,
    service_dependency=get_split_run_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.split_runs,
    tags=["SplitRuns"],
)
