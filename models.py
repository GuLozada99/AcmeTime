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

    def __le__(self, other: 'WorkTime'):
        return self < other or self == other

    def __ge__(self, other: 'WorkTime'):
        return self > other or self == other


@dataclass(frozen=True)
class WorkInterval:
    start: WorkTime
    end: WorkTime

    @staticmethod
    def is_in_between(
        interval: 'WorkInterval',
        other_interval: 'WorkInterval',
    ) -> bool:
        """Given two intervals returns whether the other_interval
        start falls in between the start and end of the interval."""
        return interval.start <= other_interval.start <= interval.end


@dataclass(frozen=True)
class Employee:
    name: str
    workdays: dict[Day, WorkInterval]

    def have_coincided(self, other: 'Employee') -> int:
        """Given another employee, returns number of times they have
        coincided in office."""
        common_days = self.get_common_days(other)
        result = 0
        for day in common_days:
            interval = self.workdays[day]
            other_interval = other.workdays[day]

            if (WorkInterval.is_in_between(interval, other_interval) or
                    WorkInterval.is_in_between(other_interval, interval)):
                result += 1
        return result

    def get_common_days(self, other: 'Employee') -> set:
        """Returns a set of common work days between two employees."""
        return self.workdays.keys() & other.workdays.keys()
