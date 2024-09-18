from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import CompetitionScoringRule
from core.schemas.competition_scoring_rule import (
    CreateCompetitionScoringRule,
    UpdateCompetitionScoringRule,
    ReadCompetitionScoringRule,
    FilterCompetitionScoringRule,
)


class CompetitionScoringRuleRepository(
    BaseRepository[
        CompetitionScoringRule,
        CreateCompetitionScoringRule,
        UpdateCompetitionScoringRule,
        FilterCompetitionScoringRule,
    ]
):
    pass


class CompetitionScoringRuleManager(
    BaseManager[
        CompetitionScoringRuleRepository,
        ReadCompetitionScoringRule,
        FilterCompetitionScoringRule,
    ]
):
    pass


class CompetitionScoringRuleService(
    BaseService[
        CompetitionScoringRuleManager,
        ReadCompetitionScoringRule,
        FilterCompetitionScoringRule,
    ]
):
    pass


(
    get_competition_scoring_rule_repo,
    getcompetition_scoring_rule_manager,
    get_competition_scoring_rule_service,
) = create_dependency_factory(
    repo_class=CompetitionScoringRuleRepository,
    manager_class=CompetitionScoringRuleManager,
    service_class=CompetitionScoringRuleService,
    model=CompetitionScoringRule,
    create_schema=CreateCompetitionScoringRule,
    update_schema=UpdateCompetitionScoringRule,
    read_schema=ReadCompetitionScoringRule,
    filter_schema=FilterCompetitionScoringRule,
)
