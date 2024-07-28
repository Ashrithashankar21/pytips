import random


def risky_calculation():
    number = random.randint(-10, 10)
    try:
        result = 100 / number
        return result
    except ZeroDivisionError:
        print("Division by zero encountered. Continuing execution...")
        return None


for _ in range(1000):
    risky_calculation()
