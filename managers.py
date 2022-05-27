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
    def create(cls, name: str, data: dict[str, str]) -> Employee:
        """Given a name and dict with keys as two-char days (DA)
        and value as interval (HH:MM-HH:MM) returns an Employee object with
        name and a workdays field which has a Day as key and WorkInterval
        as value"""
        workdays = {}
        for day, interval in data.items():
            day_object = Day[day]
            interval_object = WorkIntervalManager.create(interval)
            workdays[day_object] = interval_object

        return Employee(name, workdays)

    @classmethod
    def bulk_create(cls, employee_data: list) -> list[Employee]:
        return [cls.create(**data) for data in employee_data]

    @staticmethod
    def get_coincidences(employees: list[Employee]) -> list[str]:
        """Given a list of employees, returns a list of strings in the
        format: NAME1-NAME2: COINCIDENCES. If there are no coincidences
        between two employees, no string will be there to represent it."""
        result = []
        for i in range(len(employees)):
            employee = employees[i]
            for j in range(i + 1, len(employees)):
                other_employee = employees[j]
                if coincidence := employee.have_coincided(other_employee):
                    result.append(
                        f'{employee.name}-{other_employee.name}: {coincidence}'
                    )
        return result
