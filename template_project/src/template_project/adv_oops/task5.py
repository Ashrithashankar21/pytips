class UpperCase:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value.upper()


class Person:
    name = UpperCase("name")

    def __init__(self, name):
        self.name = name


person = Person("john doe")

if __name__ == "__main__":
    print(person.name)
    person.name = "jane doe"
    print(person.name)
