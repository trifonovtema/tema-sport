from fastapi_users import FastAPIUsers

from backend.core.models import User
from backend.dependencies.authentication.user_manager import get_user_manager
from backend.dependencies.authentication.backend import authentication_backend
from backend.settings import get_settings

fastapi_users = FastAPIUsers[User, get_settings().db.id_type.id_type](
    get_user_manager,
    [authentication_backend],
)

current_user = fastapi_users.current_user(active=True)
current_super_user = fastapi_users.current_user(superuser=True)
