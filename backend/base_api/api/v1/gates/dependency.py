from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import Gate
from core.schemas.gate import CreateGate, UpdateGate, ReadGate, FilterGate


class GateRepository(BaseRepository[Gate, CreateGate, UpdateGate, FilterGate]):
    pass


class GateManager(BaseManager[GateRepository, ReadGate, FilterGate]):
    pass


class GateService(BaseService[GateManager, ReadGate, FilterGate]):
    pass


get_gate_repo, get_gate_manager, get_gate_service = create_dependency_factory(
    repo_class=GateRepository,
    manager_class=GateManager,
    service_class=GateService,
    model=Gate,
    create_schema=CreateGate,
    update_schema=UpdateGate,
    read_schema=ReadGate,
    filter_schema=FilterGate,
)
