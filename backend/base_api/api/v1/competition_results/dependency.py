from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import LinkCompetitionResult
from core.schemas.competition_result import (
    CreateCompetitionResult,
    UpdateCompetitionResult,
    ReadCompetitionResult,
    FilterCompetitionResult,
)


class CompetitionResultRepository(
    BaseRepository[
        LinkCompetitionResult,
        CreateCompetitionResult,
        UpdateCompetitionResult,
        FilterCompetitionResult,
    ]
):
    pass


class CompetitionResultManager(
    BaseManager[
        CompetitionResultRepository, ReadCompetitionResult, FilterCompetitionResult
    ]
):
    pass


class CompetitionResultService(
    BaseService[
        CompetitionResultManager, ReadCompetitionResult, FilterCompetitionResult
    ]
):
    pass


(
    get_competition_result_repo,
    get_competition_result_manager,
    get_competition_result_service,
) = create_dependency_factory(
    repo_class=CompetitionResultRepository,
    manager_class=CompetitionResultManager,
    service_class=CompetitionResultService,
    model=LinkCompetitionResult,
    create_schema=CreateCompetitionResult,
    update_schema=UpdateCompetitionResult,
    read_schema=ReadCompetitionResult,
    filter_schema=FilterCompetitionResult,
)
