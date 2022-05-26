from models import Day, Employee, WorkInterval, WorkTime


class WorkTimeManager:
    @classmethod
    def create(cls, time: str) -> WorkTime:
        """Given a string in the format HH:MM, returns a WorkTime object
        with HH as the hour field and MM as the minute field"""
        hour, minute = map(int, time.split(':'))
        cls.validate_hour(hour)
        cls.validate_minute(minute)
        return WorkTime(hour, minute)

    @staticmethod
    def validate_hour(hour: int):
        if not (0 <= hour < 24):
            raise ValueError('Hour must be between 0 and 23')

    @staticmethod
    def validate_minute(minute: int):
        if not (0 <= minute < 59):
            raise ValueError('Minute must be between 0 and 59')


class WorkIntervalManager:
    ...


class EmployeeManager:
    ...
