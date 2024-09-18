from base_api.api.v1.gate_runs.dependency import GateRunService, get_gate_run_service
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.gate_run import CreateGateRun, UpdateGateRun, FilterGateRun
from core.config import settings


router = create_crud_router_factory(
    service_class=GateRunService,
    create_schema=CreateGateRun,
    update_schema=UpdateGateRun,
    filter_schema=FilterGateRun,
    service_dependency=get_gate_run_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.gate_runs,
    tags=["GateRuns"],
)
