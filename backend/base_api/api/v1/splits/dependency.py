from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import Split
from core.schemas.split import CreateSplit, UpdateSplit, ReadSplit, FilterSplit


class SplitRepository(BaseRepository[Split, CreateSplit, UpdateSplit, FilterSplit]):
    pass


class SplitManager(BaseManager[SplitRepository, ReadSplit, FilterSplit]):
    pass


class SplitService(BaseService[SplitManager, ReadSplit, FilterSplit]):
    pass


get_split_repo, get_split_manager, get_split_service = create_dependency_factory(
    repo_class=SplitRepository,
    manager_class=SplitManager,
    service_class=SplitService,
    model=Split,
    create_schema=CreateSplit,
    update_schema=UpdateSplit,
    read_schema=ReadSplit,
    filter_schema=FilterSplit,
)
