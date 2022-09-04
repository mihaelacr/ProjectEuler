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


primes_under_10M = list(takewhile(lambda p: p <= 10**7, primes()))


def prime_factorization(number):
    """Return the unique prime factorization of `number`

    assuming number <= 10 million

    cf the Fundamental Theorem of Arithmetic
    """
    global primes_under_10M

    assert number <= 10**7

    factors = []
    running_product = 1
    current_number = number

    # Loop through the primes, iteratively dividing our
    # number by each prime `p` so long as `p` exactly
    # divides `current_number`
    for p in primes_under_10M:
        while (current_number % p) == 0:
            current_number = current_number // p
            factors.append(p)
            running_product *= p
        if running_product == number:
            return set(factors)


def eulers_totient(n):
    # Euler's product formula
    # Using only integer maths
    numerator = 1
    denominator = 1
    for p in prime_factorization(n):
        numerator *= p - 1
        denominator *= p
    return n * numerator // denominator


if __name__ == "__main__":
    # Thoughts:
    # - n and phi(n) need to be the same magnitude to be palindromes
    # - phi(p) = p-1 for prime p
    # - For n/phi(n) to be small, want big phi(n), so n should be close to prime (probably a product of two primes?)
    # - phi(pq) = phi(p)phi(q) = (p-1)(q-1) for primes p,q

    min_n_over_phi = 10**10
    found_n = None

    for n in range(10**7, 2, -1):
        phi = int(eulers_totient(n))

        if sorted(str(phi)) == sorted(str(n)):
            n_over_phi = n / phi

            if n_over_phi < min_n_over_phi:
                min_n_over_phi = n_over_phi
                found_n = n
                print(f"phi({n})={phi}, {n_over_phi=}")

        if n % 50_000 == 0:
            print(f"Reached n = {n}")
