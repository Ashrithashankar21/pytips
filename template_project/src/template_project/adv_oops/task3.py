import time


def cache(func):
    memo = {}

    def wrapper(*args):
        if args in memo:
            return memo[args]
        result = func(*args)
        memo[args] = result
        return result

    return wrapper


@cache
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    n = 100

    start_time = time.time()
    print(f"Fibonacci({n}) = {fibonacci(n)}")
    end_time = time.time()

    print(f"Time taken: {end_time - start_time} seconds")
