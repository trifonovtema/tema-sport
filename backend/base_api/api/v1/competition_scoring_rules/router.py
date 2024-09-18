from base_api.api.v1.competition_scoring_rules.dependency import (
    CompetitionScoringRuleService,
    get_competition_scoring_rule_service,
)
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.competition_scoring_rule import (
    CreateCompetitionScoringRule,
    UpdateCompetitionScoringRule,
    FilterCompetitionScoringRule,
)
from core.config import settings


router = create_crud_router_factory(
    service_class=CompetitionScoringRuleService,
    create_schema=CreateCompetitionScoringRule,
    update_schema=UpdateCompetitionScoringRule,
    filter_schema=FilterCompetitionScoringRule,
    service_dependency=get_competition_scoring_rule_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.competition_scoring_rules,
    tags=["CompetitionScoringRules"],
)
