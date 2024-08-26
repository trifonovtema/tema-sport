from fastapi_users import FastAPIUsers

from backend.core.models import User
from backend.dependencies.authentication.user_manager import get_user_manager
from .backend import authentication_backend
from backend.core.types.user_id import UserIdType

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)
