from base_api.api.v1.bib_athletes.dependency import (
    BibAthleteService,
    get_bib_athlete_service,
)
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.bib_athlete import (
    CreateBibAthlete,
    UpdateBibAthlete,
    FilterBibAthlete,
)
from core.config import settings


router = create_crud_router_factory(
    service_class=BibAthleteService,
    create_schema=CreateBibAthlete,
    update_schema=UpdateBibAthlete,
    filter_schema=FilterBibAthlete,
    service_dependency=get_bib_athlete_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.bib_athletes,
    tags=["BibAthletes"],
)
