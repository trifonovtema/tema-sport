from base_api.api.v1.starts.dependency import StartService, get_start_service
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.start import CreateStart, UpdateStart, FilterStart
from core.config import settings


router = create_crud_router_factory(
    service_class=StartService,
    create_schema=CreateStart,
    update_schema=UpdateStart,
    filter_schema=FilterStart,
    service_dependency=get_start_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.starts,
    tags=["Starts"],
)
