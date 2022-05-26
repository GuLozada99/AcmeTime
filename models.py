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

    def __gt__(self, other: 'WorkTime'):
        return self.hour > other.hour or (self.hour == other.hour and
                                          self.minute > other.minute)

    def __lt__(self, other: 'WorkTime'):
        return self.hour < other.hour or (self.hour == other.hour and
                                          self.minute < other.minute)


@dataclass(frozen=True)
class WorkInterval:
    start: WorkTime
    end: WorkTime


@dataclass(frozen=True)
class Employee:
    name: str
    workdays: dict[Day, WorkInterval]
