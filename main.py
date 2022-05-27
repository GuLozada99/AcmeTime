import sys

from filereader import TextReader
from managers import EmployeeManager

PATH = './data.txt'


def main():
    try:
        employee_data = TextReader.get_data(PATH)
    except FileNotFoundError:
        print(f'File {PATH} does not exist')
        sys.exit(1)

    employees = EmployeeManager.bulk_create(employee_data)
    for coincidence in EmployeeManager.get_coincidences(employees):
        print(coincidence)


if __name__ == '__main__':
    main()
