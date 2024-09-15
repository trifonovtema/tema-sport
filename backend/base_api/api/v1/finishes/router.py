from base_api.api.v1.finishes.dependency import FinishService, get_finish_service
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.finish import CreateFinish, UpdateFinish, FilterFinish
from core.config import settings


router = create_crud_router_factory(
    service_class=FinishService,
    create_schema=CreateFinish,
    update_schema=UpdateFinish,
    filter_schema=FilterFinish,
    service_dependency=get_finish_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.races,
    tags=["Finishes"],
)
