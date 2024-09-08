from enum import Enum, IntEnum


class CourseElementType(str, Enum):
    GATE = "gate"
    SPLIT = "split"
    START = "start"
    FINISH = "finish"


class GateType(str, Enum):
    UPSTREAM = "upstream"
    DOWNSTREAM = "downstream"
