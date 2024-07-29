class GreetingMetaclass(type):
    def __new__(cls, name, bases, dct):
        def greet(self):
            return "Hello! This method is added by GreetingMetaclass."

        dct["greet"] = greet
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=GreetingMetaclass):
    pass


class AnotherClass:
    pass


if __name__ == "__main__":
    my_class_instance = MyClass()
    print(my_class_instance.greet())
    another_class_instance = AnotherClass()
    try:
        print(another_class_instance.greet())
    except AttributeError as e:
        print(e)
