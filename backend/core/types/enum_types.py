from enum import Enum


class CourseElementType(str, Enum):
    GATE = "gate"
    SPLIT = "split"
    START = "start"
    FINISH = "finish"


class GateType(str, Enum):
    UPSTREAM = "upstream"
    DOWNSTREAM = "downstream"
