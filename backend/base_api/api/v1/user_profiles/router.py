from base_api.api.v1.user_profiles.dependency import (
    UserProfileService,
    get_user_profile_service,
)
from core.base.crud_router_factory import create_crud_router_factory
from core.schemas.user_profile import (
    CreateUserProfile,
    UpdateUserProfile,
    FilterUserProfile,
)
from core.config import settings


router = create_crud_router_factory(
    service_class=UserProfileService,
    create_schema=CreateUserProfile,
    update_schema=UpdateUserProfile,
    filter_schema=FilterUserProfile,
    service_dependency=get_user_profile_service,
    id_type=settings.db.id_type_class.get_id_type(),
    prefix=settings.api.v1.user_profiles,
    tags=["UserProfiles"],
)
