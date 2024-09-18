from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import LinkGateCompetitorRun
from core.schemas.gate_run import (
    CreateGateRun,
    UpdateGateRun,
    ReadGateRun,
    FilterGateRun,
)


class GateRunRepository(
    BaseRepository[LinkGateCompetitorRun, CreateGateRun, UpdateGateRun, FilterGateRun]
):
    pass


class GateRunManager(BaseManager[GateRunRepository, ReadGateRun, FilterGateRun]):
    pass


class GateRunService(BaseService[GateRunManager, ReadGateRun, FilterGateRun]):
    pass


get_gate_run_repo, get_gate_run_manager, get_gate_run_service = (
    create_dependency_factory(
        repo_class=GateRunRepository,
        manager_class=GateRunManager,
        service_class=GateRunService,
        model=LinkGateCompetitorRun,
        create_schema=CreateGateRun,
        update_schema=UpdateGateRun,
        read_schema=ReadGateRun,
        filter_schema=FilterGateRun,
    )
)
