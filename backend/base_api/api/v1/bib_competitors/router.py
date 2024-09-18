from base_api.api.v1.bib_competitors.dependency import (
    BibCompetitorService,
    get_bib_competitor_service,
)
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.bib_competitor import (
    CreateBibCompetitor,
    UpdateBibCompetitor,
    FilterBibCompetitor,
)
from core.config import settings


router = create_crud_router_factory(
    service_class=BibCompetitorService,
    create_schema=CreateBibCompetitor,
    update_schema=UpdateBibCompetitor,
    filter_schema=FilterBibCompetitor,
    service_dependency=get_bib_competitor_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.bib_competitors,
    tags=["BibCompetitors"],
)
