from typing import List


def is_prime(n: int) -> bool:
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # Other even numbers are not primes
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True


def filter_primes(numbers: List[int]) -> List[int]:
    """Filter out non-prime numbers from the input list."""
    return [num for num in numbers if is_prime(num)]


if __name__ == "__main__":
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    prime_numbers = filter_primes(numbers)
    print(prime_numbers)
