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

    @classmethod
    def create(cls, interval: str) -> WorkInterval:
        """Given a string in the format HH:MM-HH:MM, returns a WorkInterval
        object with HH as the hour field and MM as the minute field"""
        start, end = map(WorkTimeManager.create, interval.split('-'))
        cls.validate_interval(start, end)
        return WorkInterval(start, end)

    @staticmethod
    def validate_interval(start: WorkTime, end: WorkTime):
        if not (start < end):
            raise ValueError('Start time must be before end')


class EmployeeManager:

    @classmethod
    def create(cls, data: str):
        """Given a string in the format NAME=DAHH:MM-HH:MM,DAHH:MM-HH:MM,
        ... returns an Employee object with name and a workdays field which has
        a Day as key and WorkInterval as value"""
        name, work_data = data.split('=')
        days_data = work_data.split(',')
        workdays = {}
        for day_data in days_data:
            day = day_data[:2]  # first 2 chars in str are day (DA)
            interval = day_data[2:]  # the rest is the interval

            day = Day[day]
            interval = WorkIntervalManager.create(interval)
            workdays[day] = interval

        return Employee(name, workdays)
