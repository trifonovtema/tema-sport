from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import Bib
from core.schemas.bib import CreateBib, UpdateBib, ReadBib, FilterBib


class BibRepository(BaseRepository[Bib, CreateBib, UpdateBib, FilterBib]):
    pass


class BibManager(BaseManager[BibRepository, ReadBib, FilterBib]):
    pass


class BibService(BaseService[BibManager, ReadBib, FilterBib]):
    pass


get_bib_repo, get_bib_manager, get_bib_service = create_dependency_factory(
    repo_class=BibRepository,
    manager_class=BibManager,
    service_class=BibService,
    model=Bib,
    create_schema=CreateBib,
    update_schema=UpdateBib,
    read_schema=ReadBib,
    filter_schema=FilterBib,
)
