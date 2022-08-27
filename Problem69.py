from itertools import takewhile
from math import sqrt


def primes():
    """Simple generator of primes by trial division"""
    yield 2
    candidate = 3
    while True:
        for i in range(3, int(sqrt(candidate)) + 1, 2):
            if (candidate % i) == 0:
                break
        else:
            yield candidate
        candidate += 2


primes_under_1M = list(takewhile(lambda p: p <= 1_000_000, primes()))


def prime_factorization(number):
    """Return the unique prime factorization of `number`

    assuming number <= 1 million

    cf the Fundamental Theorem of Arithmetic
    """
    global primes_under_1M

    assert number <= 1_000_000

    factors = []
    running_product = 1
    current_number = number

    # Loop through the primes, iteratively dividing our
    # number by each prime `p` so long as `p` exactly
    # divides `current_number`
    for p in primes_under_1M:
        while (current_number % p) == 0:
            current_number = current_number // p
            factors.append(p)
            running_product *= p
        if running_product == number:
            return set(factors)


def eulers_totient(n):
    # Euler's product formula
    phi = n
    for p in prime_factorization(n):
        phi *= 1 - 1 / p
    return phi


if __name__ == "__main__":
    max_n_over_phi = 0
    found_n = None

    for n in range(2, 1_000_001):
        n_over_phi = n / eulers_totient(n)

        if n_over_phi > max_n_over_phi:
            max_n_over_phi = n_over_phi
            found_n = n
            print(n, n_over_phi)

        if n % 50_000 == 0:
            print(f"Reached n = {n}")
