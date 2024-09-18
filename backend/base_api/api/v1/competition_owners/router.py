from base_api.api.v1.competition_owners.dependency import (
    CompetitionOwnerService,
    get_competitionowner_service,
)
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.competition_owner import (
    CreateCompetitionOwner,
    UpdateCompetitionOwner,
    FilterCompetitionOwner,
)
from core.config import settings


router = create_crud_router_factory(
    service_class=CompetitionOwnerService,
    create_schema=CreateCompetitionOwner,
    update_schema=UpdateCompetitionOwner,
    filter_schema=FilterCompetitionOwner,
    service_dependency=get_competitionowner_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.competition_owners,
    tags=["CompetitionOwners"],
)
