from dataclasses import dataclass
from enum import Enum, auto


class Day(Enum):
    SU = auto()
    MO = auto()
    TU = auto()
    WE = auto()
    TH = auto()
    FR = auto()
    SA = auto()


@dataclass(eq=True, frozen=True)
class WorkTime:
    hour: int
    minute: int
