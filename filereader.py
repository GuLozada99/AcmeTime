import abc


class Reader(abc.ABC):

    @classmethod
    @abc.abstractmethod
    def get_data(cls, path: str) -> list[dict]:
        ...


class TextReader(Reader):

    @classmethod
    def get_data(cls, path: str) -> list[dict]:
        with open(path) as f:
            result = []
            for line in f.readlines():
                name, work_data = line.split('=')
                days_data = work_data.split(',')
                employee_info = {
                    'name': name,
                    'data': {}
                }
                for day_data in days_data:
                    day = day_data[:2]  # first 2 chars in str are day (DA)
                    interval = day_data[2:]  # the rest is the interval
                    employee_info['data'][day] = interval
                employee_info['name'] = name
                result.append(employee_info.copy())
            return result
