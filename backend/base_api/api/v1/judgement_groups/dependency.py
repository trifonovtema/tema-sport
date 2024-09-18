from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import JudgementGroup
from core.schemas.judgement_group import (
    CreateJudgementGroup,
    UpdateJudgementGroup,
    ReadJudgementGroup,
    FilterJudgementGroup,
)


class JudgementGroupRepository(
    BaseRepository[
        JudgementGroup, CreateJudgementGroup, UpdateJudgementGroup, FilterJudgementGroup
    ]
):
    pass


class JudgementGroupManager(
    BaseManager[JudgementGroupRepository, ReadJudgementGroup, FilterJudgementGroup]
):
    pass


class JudgementGroupService(
    BaseService[JudgementGroupManager, ReadJudgementGroup, FilterJudgementGroup]
):
    pass


get_judgement_group_repo, get_judgement_group_manager, get_judgement_group_service = (
    create_dependency_factory(
        repo_class=JudgementGroupRepository,
        manager_class=JudgementGroupManager,
        service_class=JudgementGroupService,
        model=JudgementGroup,
        create_schema=CreateJudgementGroup,
        update_schema=UpdateJudgementGroup,
        read_schema=ReadJudgementGroup,
        filter_schema=FilterJudgementGroup,
    )
)
