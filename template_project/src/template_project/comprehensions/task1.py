import json
import random

file_path = (
    "C:/Users/ashritha.shankar/python/python/template_project/src/"
    "template_project/comprehensions/data.json"
)

data = [{"id": i, "value": random.randint(1, 100)} for i in range(10001)]
json.dump(data, open(file_path, "w"))

with open(file_path, "r") as file:
    data = json.load(file)


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


squared_primes = [item["value"] ** 2 for item in data if is_prime(item["value"])]

unique_squared_primes = {value for value in squared_primes}

print(f"Total squared prime values: {len(squared_primes)}")
print(f"Unique squared prime values: {len(unique_squared_primes)}")
