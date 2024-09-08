from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import Run
from core.schemas.run import CreateRun, UpdateRun, ReadRun, FilterRun


class RunRepository(BaseRepository[Run, CreateRun, UpdateRun, FilterRun]):
    pass


class RunManager(BaseManager[RunRepository, ReadRun, FilterRun]):
    pass


class RunService(BaseService[RunManager, ReadRun, FilterRun]):
    pass


get_run_repo, get_run_manager, get_run_service = create_dependency_factory(
    repo_class=RunRepository,
    manager_class=RunManager,
    service_class=RunService,
    model=Run,
    create_schema=CreateRun,
    update_schema=UpdateRun,
    read_schema=ReadRun,
    filter_schema=FilterRun,
)
