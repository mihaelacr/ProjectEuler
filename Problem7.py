from math import sqrt
from itertools import islice


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


def nth_prime(n):
    """Get the nth prime number (for 1-based n)

    Uses islice to index into the primes() generator
    """
    return next(islice(primes(), n - 1, None))


if __name__ == "__main__":
    print(nth_prime(10_001))
