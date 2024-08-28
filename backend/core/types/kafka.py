from enum import Enum


class MessageType(str, Enum):
    USERS_ADD = "user_add"
    USERS_UPDATE = "user_update"
    USERS_DELETE = "user_delete"
    USERS_GET = "user_get"
    COMPETITIONS_ADD = "competitions_add"
    COMPETITIONS_UPDATE = "competitions_update"
    COMPETITIONS_DELETE = "competitions_delete"
    COMPETITIONS_GET = "competitions_get"
