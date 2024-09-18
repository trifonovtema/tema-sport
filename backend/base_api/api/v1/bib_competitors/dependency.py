from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import LinkBibCompetitor
from core.schemas.bib_competitor import (
    CreateBibCompetitor,
    UpdateBibCompetitor,
    ReadBibCompetitor,
    FilterBibCompetitor,
)


class BibCompetitorRepository(
    BaseRepository[
        LinkBibCompetitor, CreateBibCompetitor, UpdateBibCompetitor, FilterBibCompetitor
    ]
):
    pass


class BibCompetitorManager(
    BaseManager[BibCompetitorRepository, ReadBibCompetitor, FilterBibCompetitor]
):
    pass


class BibCompetitorService(
    BaseService[BibCompetitorManager, ReadBibCompetitor, FilterBibCompetitor]
):
    pass


get_bib_competitor_repo, get_bib_competitor_manager, get_bib_competitor_service = (
    create_dependency_factory(
        repo_class=BibCompetitorRepository,
        manager_class=BibCompetitorManager,
        service_class=BibCompetitorService,
        model=LinkBibCompetitor,
        create_schema=CreateBibCompetitor,
        update_schema=UpdateBibCompetitor,
        read_schema=ReadBibCompetitor,
        filter_schema=FilterBibCompetitor,
    )
)
