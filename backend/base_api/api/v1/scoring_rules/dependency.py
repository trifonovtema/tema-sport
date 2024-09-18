from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import ScoringRule
from core.schemas.scoring_rule import (
    CreateScoringRule,
    UpdateScoringRule,
    ReadScoringRule,
    FilterScoringRule,
)


class ScoringRuleRepository(
    BaseRepository[ScoringRule, CreateScoringRule, UpdateScoringRule, FilterScoringRule]
):
    pass


class ScoringRuleManager(
    BaseManager[ScoringRuleRepository, ReadScoringRule, FilterScoringRule]
):
    pass


class ScoringRuleService(
    BaseService[ScoringRuleManager, ReadScoringRule, FilterScoringRule]
):
    pass


get_scoring_rule_repo, get_scoring_rule_manager, get_scoring_rule_service = (
    create_dependency_factory(
        repo_class=ScoringRuleRepository,
        manager_class=ScoringRuleManager,
        service_class=ScoringRuleService,
        model=ScoringRule,
        create_schema=CreateScoringRule,
        update_schema=UpdateScoringRule,
        read_schema=ReadScoringRule,
        filter_schema=FilterScoringRule,
    )
)
