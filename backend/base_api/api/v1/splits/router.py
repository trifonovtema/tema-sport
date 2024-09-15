from base_api.api.v1.splits.dependency import SplitService, get_split_service
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.split import CreateSplit, UpdateSplit, FilterSplit
from core.config import settings


router = create_crud_router_factory(
    service_class=SplitService,
    create_schema=CreateSplit,
    update_schema=UpdateSplit,
    filter_schema=FilterSplit,
    service_dependency=get_split_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.splits,
    tags=["Splits"],
)
