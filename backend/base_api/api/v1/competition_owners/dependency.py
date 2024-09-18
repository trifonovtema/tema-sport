from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import LinkCompetitionOwner
from core.schemas.competition_owner import (
    CreateCompetitionOwner,
    UpdateCompetitionOwner,
    ReadCompetitionOwner,
    FilterCompetitionOwner,
)


class CompetitionOwnerRepository(
    BaseRepository[
        LinkCompetitionOwner,
        CreateCompetitionOwner,
        UpdateCompetitionOwner,
        FilterCompetitionOwner,
    ]
):
    pass


class CompetitionOwnerManager(
    BaseManager[
        CompetitionOwnerRepository, ReadCompetitionOwner, FilterCompetitionOwner
    ]
):
    pass


class CompetitionOwnerService(
    BaseService[CompetitionOwnerManager, ReadCompetitionOwner, FilterCompetitionOwner]
):
    pass


(
    get_competitionowner_repo,
    get_competitionowner_manager,
    get_competitionowner_service,
) = create_dependency_factory(
    repo_class=CompetitionOwnerRepository,
    manager_class=CompetitionOwnerManager,
    service_class=CompetitionOwnerService,
    model=LinkCompetitionOwner,
    create_schema=CreateCompetitionOwner,
    update_schema=UpdateCompetitionOwner,
    read_schema=ReadCompetitionOwner,
    filter_schema=FilterCompetitionOwner,
)
