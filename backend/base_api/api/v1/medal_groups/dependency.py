from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import MedalGroup
from core.schemas.medal_group import (
    CreateMedalGroup,
    UpdateMedalGroup,
    ReadMedalGroup,
    FilterMedalGroup,
)


class MedalGroupRepository(
    BaseRepository[MedalGroup, CreateMedalGroup, UpdateMedalGroup, FilterMedalGroup]
):
    pass


class MedalGroupManager(
    BaseManager[MedalGroupRepository, ReadMedalGroup, FilterMedalGroup]
):
    pass


class MedalGroupService(
    BaseService[MedalGroupManager, ReadMedalGroup, FilterMedalGroup]
):
    pass


get_medal_group_repo, get_medal_group_manager, get_medal_group_service = (
    create_dependency_factory(
        repo_class=MedalGroupRepository,
        manager_class=MedalGroupManager,
        service_class=MedalGroupService,
        model=MedalGroup,
        create_schema=CreateMedalGroup,
        update_schema=UpdateMedalGroup,
        read_schema=ReadMedalGroup,
        filter_schema=FilterMedalGroup,
    )
)
