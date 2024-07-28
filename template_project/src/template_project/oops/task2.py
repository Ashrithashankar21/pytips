from task1 import Employee


class Manager(Employee):
    def __init__(self, employee_id: int, name: str, salary: float):
        super().__init__(employee_id, name, "Manager", salary)

    def promote(self, employee: Employee, increase: float):
        if increase < 0:
            raise ValueError("Increase amount cannot be negative")
        employee.salary += increase
        print(f" New salary: {employee.salary}")


class Developer(Employee):
    def __init__(self, employee_id: int, name: str, salary: float, lang: str):
        super().__init__(employee_id, name, "Developer", salary)
        self.programming_language = lang

    def code(self):
        print(f"{self.name} is coding in {self.programming_language}")


class Intern(Employee):
    def __init__(self, employee_id: int, name: str, sal: float, duration: int):
        super().__init__(employee_id, name, "Intern", sal)
        self.duration = duration  # Duration in months

    def extend_internship(self, additional_months: int):
        if additional_months < 0:
            raise ValueError("Additional months cannot be negative")
        self.duration += additional_months
        print(f"New duration: {self.duration} months")


if __name__ == "__main__":
    mgr = Manager(1, "Alice", 90000)
    dev = Developer(2, "Bob", 80000, "Python")
    intern = Intern(3, "Charlie", 30000, 6)

    print(mgr)
    print(dev)
    print(intern)

    mgr.promote(dev, 5000)

    dev.code()

    intern.extend_internship(3)

    print(f"Total number of employees: {Employee.get_employee_count()}")
