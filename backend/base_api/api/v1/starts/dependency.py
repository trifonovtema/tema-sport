from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import Start
from core.schemas.start import CreateStart, UpdateStart, ReadStart, FilterStart


class StartRepository(BaseRepository[Start, CreateStart, UpdateStart, FilterStart]):
    pass


class StartManager(BaseManager[StartRepository, ReadStart, FilterStart]):
    pass


class StartService(BaseService[StartManager, ReadStart, FilterStart]):
    pass


get_start_repo, get_start_manager, get_start_service = create_dependency_factory(
    repo_class=StartRepository,
    manager_class=StartManager,
    service_class=StartService,
    model=Start,
    create_schema=CreateStart,
    update_schema=UpdateStart,
    read_schema=ReadStart,
    filter_schema=FilterStart,
)
