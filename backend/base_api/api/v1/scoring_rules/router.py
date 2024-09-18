from base_api.api.v1.scoring_rules.dependency import (
    ScoringRuleService,
    get_scoring_rule_service,
)
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.scoring_rule import (
    CreateScoringRule,
    UpdateScoringRule,
    FilterScoringRule,
)
from core.config import settings


router = create_crud_router_factory(
    service_class=ScoringRuleService,
    create_schema=CreateScoringRule,
    update_schema=UpdateScoringRule,
    filter_schema=FilterScoringRule,
    service_dependency=get_scoring_rule_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.scoring_rules,
    tags=["ScoringRules"],
)
