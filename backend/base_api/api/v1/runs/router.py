from base_api.api.v1.runs.dependency import RunService, get_run_service
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.run import CreateRun, UpdateRun, FilterRun
from core.config import settings


router = create_crud_router_factory(
    service_class=RunService,
    create_schema=CreateRun,
    update_schema=UpdateRun,
    filter_schema=FilterRun,
    service_dependency=get_run_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.runs,
    tags=["Runs"],
)
