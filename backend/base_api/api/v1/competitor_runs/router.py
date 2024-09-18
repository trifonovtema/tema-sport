from base_api.api.v1.competitor_runs.dependency import (
    CompetitorRunService,
    get_competitor_run_service,
)
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.competitor_run import (
    CreateCompetitorRun,
    UpdateCompetitorRun,
    FilterCompetitorRun,
)
from core.config import settings


router = create_crud_router_factory(
    service_class=CompetitorRunService,
    create_schema=CreateCompetitorRun,
    update_schema=UpdateCompetitorRun,
    filter_schema=FilterCompetitorRun,
    service_dependency=get_competitor_run_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.competitor_runs,
    tags=["CompetitorRuns"],
)
