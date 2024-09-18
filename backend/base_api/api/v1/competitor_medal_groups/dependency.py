from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import LinkCompetitorMedalGroup
from core.schemas.competitor_medal_group import (
    CreateCompetitorMedalGroup,
    UpdateCompetitorMedalGroup,
    ReadCompetitorMedalGroup,
    FilterCompetitorMedalGroup,
)


class CompetitorMedalGroupRepository(
    BaseRepository[
        LinkCompetitorMedalGroup,
        CreateCompetitorMedalGroup,
        UpdateCompetitorMedalGroup,
        FilterCompetitorMedalGroup,
    ]
):
    pass


class CompetitorMedalGroupManager(
    BaseManager[
        CompetitorMedalGroupRepository,
        ReadCompetitorMedalGroup,
        FilterCompetitorMedalGroup,
    ]
):
    pass


class CompetitorMedalGroupService(
    BaseService[
        CompetitorMedalGroupManager,
        ReadCompetitorMedalGroup,
        FilterCompetitorMedalGroup,
    ]
):
    pass


(
    get_competitor_medal_group_repo,
    get_competitor_medal_group_manager,
    get_competitor_medal_group_service,
) = create_dependency_factory(
    repo_class=CompetitorMedalGroupRepository,
    manager_class=CompetitorMedalGroupManager,
    service_class=CompetitorMedalGroupService,
    model=LinkCompetitorMedalGroup,
    create_schema=CreateCompetitorMedalGroup,
    update_schema=UpdateCompetitorMedalGroup,
    read_schema=ReadCompetitorMedalGroup,
    filter_schema=FilterCompetitorMedalGroup,
)
