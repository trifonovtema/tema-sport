from base_api.api.v1.competition_registered_users.dependency import (
    CompetitionRegisteredUserService,
    get_competition_registered_user_service,
)
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.competition_registered_user import (
    CreateCompetitionRegisteredUser,
    UpdateCompetitionRegisteredUser,
    FilterCompetitionRegisteredUser,
)
from core.config import settings


router = create_crud_router_factory(
    service_class=CompetitionRegisteredUserService,
    create_schema=CreateCompetitionRegisteredUser,
    update_schema=UpdateCompetitionRegisteredUser,
    filter_schema=FilterCompetitionRegisteredUser,
    service_dependency=get_competition_registered_user_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.competition_registered_users,
    tags=["CompetitionRegisteredUsers"],
)
