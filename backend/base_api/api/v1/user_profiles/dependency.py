from core.base.base_manager import BaseManager
from core.base.base_repo import BaseRepository
from core.base.base_service import BaseService
from core.base.create_dependencies_factory import create_dependency_factory
from core.models import UserProfile
from core.schemas.user_profile import (
    CreateUserProfile,
    UpdateUserProfile,
    ReadUserProfile,
    FilterUserProfile,
)


class UserProfileRepository(
    BaseRepository[UserProfile, CreateUserProfile, UpdateUserProfile, FilterUserProfile]
):
    pass


class UserProfileManager(
    BaseManager[UserProfileRepository, ReadUserProfile, FilterUserProfile]
):
    pass


class UserProfileService(
    BaseService[UserProfileManager, ReadUserProfile, FilterUserProfile]
):
    pass


get_user_profile_repo, get_user_profile_manager, get_user_profile_service = (
    create_dependency_factory(
        repo_class=UserProfileRepository,
        manager_class=UserProfileManager,
        service_class=UserProfileService,
        model=UserProfile,
        create_schema=CreateUserProfile,
        update_schema=UpdateUserProfile,
        read_schema=ReadUserProfile,
        filter_schema=FilterUserProfile,
    )
)
