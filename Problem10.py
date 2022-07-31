from math import sqrt
from itertools import takewhile


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


def primes_less_than(n):
    yield from takewhile(lambda x: x < n, primes())


print(sum(primes_less_than(2_000_000)))
