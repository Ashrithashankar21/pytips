from task1 import Employee
from datetime import datetime


class Employee_1(Employee):
    @classmethod
    def from_string(cls, employee_str: str):
        employee_id, name, position, salary = employee_str.split(",")
        return cls(int(employee_id), name, position, float(salary))

    @staticmethod
    def is_workday(date: datetime):
        return date.weekday() < 5


if __name__ == "__main__":
    emp_str1 = "1,John Doe,Manager,100000"
    emp_str2 = "2,Jane Smith,Developer,85000"

    emp1 = Employee_1.from_string(emp_str1)
    emp2 = Employee_1.from_string(emp_str2)

    print(emp1)
    print(emp2)

    date1 = datetime(2024, 7, 29)
    date2 = datetime(2024, 7, 27)

    print(f"{Employee_1.is_workday(date1)}")
    print(f"{Employee_1.is_workday(date2)}")

    print(f"Total number of employees: {Employee_1.get_employee_count()}")
