def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


def calculate(operation, x, y):
    return operation(x, y)


def main():
    x, y = 10, 5

    print(f"Addition: {x} + {y} = {calculate(add, x, y)}")
    print(f"Subtraction: {x} - {y} = {calculate(subtract, x, y)}")
    print(f"Multiplication: {x} * {y} = {calculate(multiply, x, y)}")
    print(f"Division: {x} / {y} = {calculate(divide, x, y)}")


if __name__ == "__main__":
    main()
