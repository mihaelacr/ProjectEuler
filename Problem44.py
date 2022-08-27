import numpy as np


def pentagonal(n):
    assert n >= 1
    return n * (3 * n - 1) // 2


def inverse_pentagonal(p):
    return (0.5 + np.sqrt(0.25 + 6 * p)) / 3.0


def is_pentagonal(p):
    # Will have precision issues if the
    # floats get too large
    pentagonal_inv = inverse_pentagonal(p)
    return float(pentagonal_inv).is_integer()


pdiffs = []

maxN = 5000

for n1 in range(1, maxN):
    for n2 in range(1, maxN):
        p1 = pentagonal(n1)
        p2 = pentagonal(n2)

        if n2 >= n1:
            break

        assert p1 > p2

        psum = p1 + p2
        nsum = inverse_pentagonal(psum)

        pdiff = p1 - p2
        ndiff = inverse_pentagonal(pdiff)

        if is_pentagonal(psum) and is_pentagonal(pdiff):
            print(f"p{n1} + p{n2} = {p1} + {p2} = {psum} = p{nsum}")
            print(f"p{n1} - p{n2} = {p1} - {p2} = {pdiff} = p{ndiff}")
            print()
            pdiffs.append(pdiff)


print(min(pdiffs))
