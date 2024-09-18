from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import LinkBibAthlete
from core.schemas.bib_athlete import (
    CreateBibAthlete,
    UpdateBibAthlete,
    ReadBibAthlete,
    FilterBibAthlete,
)


class BibAthleteRepository(
    BaseRepository[LinkBibAthlete, CreateBibAthlete, UpdateBibAthlete, FilterBibAthlete]
):
    pass


class BibAthleteManager(
    BaseManager[BibAthleteRepository, ReadBibAthlete, FilterBibAthlete]
):
    pass


class BibAthleteService(
    BaseService[BibAthleteManager, ReadBibAthlete, FilterBibAthlete]
):
    pass


get_bib_athlete_repo, get_bib_athlete_manager, get_bib_athlete_service = (
    create_dependency_factory(
        repo_class=BibAthleteRepository,
        manager_class=BibAthleteManager,
        service_class=BibAthleteService,
        model=LinkBibAthlete,
        create_schema=CreateBibAthlete,
        update_schema=UpdateBibAthlete,
        read_schema=ReadBibAthlete,
        filter_schema=FilterBibAthlete,
    )
)
