import math
from fractions import Fraction
from itertools import islice
import numpy as np


def contfrac_sqrt_periodic(D):
    """Continued fraction representation of sqrt(D).

    Expressed as whole_part, periodic_part, eg:

    >>> contfrac_sqrt_periodic(13)
    (3, [1, 1, 1, 1, 6])

    Adapted from the solution for Problem 66,
    which I did first!
    """
    r = 0
    s = 1
    sqrt_float = math.sqrt(D)
    whole = int(sqrt_float)

    if sqrt_float.is_integer():
        # Already a perfect square
        return (whole, [])

    # This is the same as in Problem 66,
    # sequentially going from
    # (sqrt(D) + r)/s to a + (sqrt(D)-(a*s-r))/s
    # then reciprocate the fraction and mul
    # by (sqrt(D) + r_new)/(sqrt(D) + r_new)
    # where r_new = a * s - r and continue
    #
    # Except now I cache the values of (a,r,s)
    # in order to identify when the iterative
    # procedure is about to repeat itself, and
    # then I know it should stop.
    #
    # See
    # https://math.stackexchange.com/a/980515
    # https://math.stackexchange.com/a/442561
    seen = set()
    partial_denominators = []
    while True:
        a = (r + whole) // s
        r = a * s - r
        s = (D - r * r) // s

        if (a, r, s) in seen:
            break

        seen.add((a, r, s))
        partial_denominators.append(a)
    whole_part = partial_denominators[0]
    periodic_part = partial_denominators[1:]
    return whole_part, periodic_part


if __name__ == "__main__":
    n_odd_period = 0
    N_max = 10_000
    for x in range(1, N_max + 1):
        if math.sqrt(x).is_integer():
            continue
        whole, periodic = contfrac_sqrt_periodic(x)
        period = len(periodic)
        print(x, whole, periodic, period)
        n_odd_period += int((period % 2) != 0)
        print(f"Number with odd period is {n_odd_period}")
