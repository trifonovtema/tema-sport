from base_api.api.v1.gates.dependency import GateService, get_gate_service
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.gate import CreateGate, UpdateGate, FilterGate
from core.config import settings


router = create_crud_router_factory(
    service_class=GateService,
    create_schema=CreateGate,
    update_schema=UpdateGate,
    filter_schema=FilterGate,
    service_dependency=get_gate_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.gates,
    tags=["Gates"],
)
