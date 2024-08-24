from enum import Enum, IntEnum


class KafkaTopic(str, Enum):
    USERS = "users"
    WEBSOCKET = "websocket"
    COMPETITIONS = "competitions"


class MessageType(str, Enum):
    USERS_ADD = "user_add"
    USERS_UPDATE = "user_update"
    USERS_DELETE = "user_delete"
    USERS_GET = "user_get"
    COMPETITIONS_ADD = "competitions_add"
    COMPETITIONS_UPDATE = "competitions_update"
    COMPETITIONS_DELETE = "competitions_delete"
    COMPETITIONS_GET = "competitions_get"


class APIResponseStatus(str, Enum):
    SUCCESS = "OK"
    ERROR = "ERROR"


class ResponseStatus(str, Enum):
    SUCCESS = "OK"
    ERROR = "ERROR"


class GroupId(str, Enum):
    DB_STORAGE = "db_storage"
    BASE_API = "base_api"


class Tags(str, Enum):
    SUCCESS = "OK"
    ERROR = "ERROR"


class Penalty(IntEnum):
    NO = 0
    TOUCH = 2
    MISS = 50


class SplitType(str, Enum):
    START = "start"
    FINISH = "finish"
    INTERMEDIATE = "intermediate"


class CourseSegmentType(str, Enum):
    GATE = "gate"
    SPLIT = "split"
    START = "start"
    FINISH = "finish"
