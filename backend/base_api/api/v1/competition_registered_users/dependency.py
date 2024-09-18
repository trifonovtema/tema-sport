from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import LinkCompetitionRegisteredUser
from core.schemas.competition_registered_user import (
    CreateCompetitionRegisteredUser,
    UpdateCompetitionRegisteredUser,
    ReadCompetitionRegisteredUser,
    FilterCompetitionRegisteredUser,
)


class CompetitionRegisteredUserRepository(
    BaseRepository[
        LinkCompetitionRegisteredUser,
        CreateCompetitionRegisteredUser,
        UpdateCompetitionRegisteredUser,
        FilterCompetitionRegisteredUser,
    ]
):
    pass


class CompetitionRegisteredUserManager(
    BaseManager[
        CompetitionRegisteredUserRepository,
        ReadCompetitionRegisteredUser,
        FilterCompetitionRegisteredUser,
    ]
):
    pass


class CompetitionRegisteredUserService(
    BaseService[
        CompetitionRegisteredUserManager,
        ReadCompetitionRegisteredUser,
        FilterCompetitionRegisteredUser,
    ]
):
    pass


(
    get_competition_registered_user_repo,
    get_competition_registered_user_manager,
    get_competition_registered_user_service,
) = create_dependency_factory(
    repo_class=CompetitionRegisteredUserRepository,
    manager_class=CompetitionRegisteredUserManager,
    service_class=CompetitionRegisteredUserService,
    model=LinkCompetitionRegisteredUser,
    create_schema=CreateCompetitionRegisteredUser,
    update_schema=UpdateCompetitionRegisteredUser,
    read_schema=ReadCompetitionRegisteredUser,
    filter_schema=FilterCompetitionRegisteredUser,
)
