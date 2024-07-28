class Employee:
    _employee_count = 0  # Class attribute to track the number of employees

    def __init__(self, employee_id: int, name: str, pos: str, salary: float):
        self.employee_id = employee_id
        self.name = name
        self.position = pos
        self._salary = salary  # Private attribute
        Employee._employee_count += 1

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary: float):
        if new_salary >= 0:
            self._salary = new_salary
        else:
            raise ValueError("Salary cannot be negative")

    def __str__(self):
        return f"Employee ID: {self.employee_id}, \
    Name: {self.name}, Position: {self.position}, Salary: {self._salary}"

    @classmethod
    def get_employee_count(cls):
        return cls._employee_count


if __name__ == "__main__":
    emp1 = Employee(1, "Alice", "Developer", 70000)
    emp2 = Employee(2, "Bob", "Designer", 65000)
    emp3 = Employee(3, "Charlie", "Manager", 90000)

    print(emp1)
    print(emp2)
    print(emp3)

    emp1.salary = 75000
    print(f"Updated salary for {emp1.name}: {emp1.salary}")

    try:
        emp2.salary = -5000
    except ValueError as e:
        print(e)

    print(f"Total number of employees: {Employee.get_employee_count()}")
