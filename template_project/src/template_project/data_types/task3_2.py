def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"{n}! = {factorial(n)}")
