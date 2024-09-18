from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import Bib
from core.schemas.bib_pool import (
    CreateBibPool,
    UpdateBibPool,
    ReadBibPool,
    FilterBibPool,
)


class BibRepository(BaseRepository[Bib, CreateBibPool, UpdateBibPool, FilterBibPool]):
    pass


class BibManager(BaseManager[BibRepository, ReadBibPool, FilterBibPool]):
    pass


class BibService(BaseService[BibManager, ReadBibPool, FilterBibPool]):
    pass


get_bib_pool_repo, get_bib_pool_manager, get_bib_pool_service = (
    create_dependency_factory(
        repo_class=BibRepository,
        manager_class=BibManager,
        service_class=BibService,
        model=Bib,
        create_schema=CreateBibPool,
        update_schema=UpdateBibPool,
        read_schema=ReadBibPool,
        filter_schema=FilterBibPool,
    )
)
