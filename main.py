import sys

from filereader import TextReader
from managers import EmployeeManager

PATH = './data.txt'


def main():
    path = sys.argv[1] if sys.argv[1:] else PATH

    try:
        employee_data = TextReader.get_data(path)
    except FileNotFoundError:
        print(f'File {path} does not exist')
        sys.exit(1)

    employees = EmployeeManager.bulk_create(employee_data)
    for coincidence in EmployeeManager.get_coincidences(employees):
        print(coincidence)


if __name__ == '__main__':
    main()
