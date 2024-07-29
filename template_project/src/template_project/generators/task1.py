def is_prime(n):
    """Check if a number is a prime number."""
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


def prime_generator():
    """Generator that yields prime numbers indefinitely."""
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


def first_n_primes(n):
    primes = []
    gen = prime_generator()
    for _ in range(n):
        primes.append(next(gen))
    return primes


print(first_n_primes(100))
