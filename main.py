from filereader import TextReader
from managers import EmployeeManager

PATH = './data.txt'


def main():
    employee_data = TextReader.get_data(PATH)
    employees = EmployeeManager.bulk_create(employee_data)
    for coincidence in EmployeeManager.get_coincidences(employees):
        print(coincidence)


if __name__ == '__main__':
    main()
