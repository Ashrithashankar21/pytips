class InvalidAgeException(Exception):
    def __init__(self, message="Age cannot be zero or negative"):
        self.message = message
        super().__init__(self.message)


def validate_user_age(age):
    if age <= 0:
        raise InvalidAgeException("Age must be greater than zero")
    if age > 13:
        return False
    return True


if __name__ == "__main__":
    test_ages = [15, 13, 10, 0, -5]

    for age in test_ages:
        try:
            result = validate_user_age(age)
            print(f"Age {age} is valid: {result}")
        except InvalidAgeException as e:
            print(f"Invalid age {age}: {e}")
