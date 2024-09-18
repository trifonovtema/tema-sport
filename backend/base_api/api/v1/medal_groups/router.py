from base_api.api.v1.medal_groups.dependency import (
    MedalGroupService,
    get_medal_group_service,
)
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.medal_group import (
    CreateMedalGroup,
    UpdateMedalGroup,
    FilterMedalGroup,
)
from core.config import settings


router = create_crud_router_factory(
    service_class=MedalGroupService,
    create_schema=CreateMedalGroup,
    update_schema=UpdateMedalGroup,
    filter_schema=FilterMedalGroup,
    service_dependency=get_medal_group_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.medal_groups,
    tags=["MedalGroups"],
)
