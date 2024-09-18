from base_api.api.v1.bibs.dependency import BibService, get_bib_service
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.bib import CreateBib, UpdateBib, FilterBib
from core.config import settings


router = create_crud_router_factory(
    service_class=BibService,
    create_schema=CreateBib,
    update_schema=UpdateBib,
    filter_schema=FilterBib,
    service_dependency=get_bib_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.bibs,
    tags=["Bibs"],
)
