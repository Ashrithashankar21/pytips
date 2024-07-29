import time

import functools
import datetime

file_path = (
    "C:/Users/ashritha.shankar/python/python/template_project/src/"
    "template_project/adv_oops/data.json"
)


def profile_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.4f} seconds ")
        return result

    return wrapper


def log_function_call(filename=file_path):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Call the decorated function
            result = func(*args, **kwargs)

            # Log details to a file
            with open(filename, "a") as file:
                log_entry = (
                    f"{datetime.datetime.now()}: Function '{func.__name__}' "
                    f"called with arguments {args} and keyword arguments {kwargs}. "
                    f"Returned {result}\n"
                )
                file.write(log_entry)

            return result

        return wrapper

    return decorator


@profile_execution
@log_function_call()
def add(a, b):
    return a + b


@profile_execution
@log_function_call()
def multiply(x, y):
    time.sleep(1)
    return x * y


@profile_execution
@log_function_call()
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print(add(5, 7))
print(multiply(3, 4))
print(greet("Alice", "Hi"))
