import asyncio
import contextlib

from backend.core.authentication.user_manager import UserManager
from backend.core.models import db_helper, User
from backend.dependencies.authentication.users import get_users_db
from backend.core.schemas.user import UserCreate
from backend.dependencies.authentication.user_manager import get_user_manager


from fastapi_users.exceptions import UserAlreadyExists

get_user_db_context = contextlib.asynccontextmanager(get_users_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)

default_email = "admin@admin.com"
default_password = "admin"
default_is_active = True
default_is_superuser = True
default_is_verified = True


async def create_user(
    user_manager: UserManager,
    user_create: UserCreate,
) -> User:
    user = await user_manager.create(
        user_create=user_create,
        safe=False,
    )
    return user


async def create_superuser(
    email: str = default_email,
    password: str = default_password,
    is_active: bool = default_is_active,
    is_superuser: bool = default_is_superuser,
    is_verified: bool = default_is_verified,
):
    try:
        user_create = UserCreate(
            email=email,
            password=password,
            is_active=is_active,
            is_superuser=is_superuser,
            is_verified=is_verified,
        )
        async with db_helper.session_factory() as session:
            async with get_user_db_context(session) as users_db:
                async with get_user_manager_context(users_db) as user_manager:
                    return await create_user(
                        user_manager=user_manager,
                        user_create=user_create,
                    )
    except UserAlreadyExists:
        print(f"SuperUser already exists")


if __name__ == "__main__":
    asyncio.run(create_superuser())
