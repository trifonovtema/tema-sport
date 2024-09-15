from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import Finish
from core.schemas.finish import CreateFinish, UpdateFinish, ReadFinish, FilterFinish


class FinishRepository(
    BaseRepository[Finish, CreateFinish, UpdateFinish, FilterFinish]
):
    pass


class FinishManager(BaseManager[FinishRepository, ReadFinish, FilterFinish]):
    pass


class FinishService(BaseService[FinishManager, ReadFinish, FilterFinish]):
    pass


get_finish_repo, get_finish_manager, get_finish_service = create_dependency_factory(
    repo_class=FinishRepository,
    manager_class=FinishManager,
    service_class=FinishService,
    model=Finish,
    create_schema=CreateFinish,
    update_schema=UpdateFinish,
    read_schema=ReadFinish,
    filter_schema=FilterFinish,
)
