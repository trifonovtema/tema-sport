from base_api.api.v1.judgement_groups.dependency import (
    JudgementGroupService,
    get_judgement_group_service,
)
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.judgement_group import (
    CreateJudgementGroup,
    UpdateJudgementGroup,
    FilterJudgementGroup,
)
from core.config import settings


router = create_crud_router_factory(
    service_class=JudgementGroupService,
    create_schema=CreateJudgementGroup,
    update_schema=UpdateJudgementGroup,
    filter_schema=FilterJudgementGroup,
    service_dependency=get_judgement_group_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.judgement_groups,
    tags=["JudgementGroups"],
)
