import json


class JsonSerializableMixin:
    def to_json(self):
        return json.dumps(self.__dict__)


class Person(JsonSerializableMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Alice", 30)

if __name__ == "__main__":
    json_string = person.to_json()
    print(json_string)
