from base_api.api.v1.competitor_medal_groups.dependency import (
    CompetitorMedalGroupService,
    get_competitor_medal_group_service,
)
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.competitor_medal_group import (
    CreateCompetitorMedalGroup,
    UpdateCompetitorMedalGroup,
    FilterCompetitorMedalGroup,
)
from core.config import settings


router = create_crud_router_factory(
    service_class=CompetitorMedalGroupService,
    create_schema=CreateCompetitorMedalGroup,
    update_schema=UpdateCompetitorMedalGroup,
    filter_schema=FilterCompetitorMedalGroup,
    service_dependency=get_competitor_medal_group_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.competitor_medal_groups,
    tags=["CompetitorMedalGroups"],
)
