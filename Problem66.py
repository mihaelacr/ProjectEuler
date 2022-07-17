import math
from fractions import Fraction
from itertools import islice
import numpy as np

# We want to find integer solutions x,y to
# x**2 - D*y**2 = 1
# for minimal x and
# for non-square integer D, 2 <= D <= 1000
#
# and then find the D which gives maxium x
#
# this is Pell's equation
# https://en.wikipedia.org/wiki/Pell%27s_equation
# which can be solved using continued fraction
# representation of sqrt(D), where x/y will appear
# in the sequence of convergents of the continued
# fraction


def contfrac_inaccurate(n):
    """This is the naive way of generating continuous fraction terms,
    but quickly becomes inaccurate due to the use of floating point
    arithmetic
    """
    while True:
        whole = int(n)
        yield whole
        remainder = n - int(n)
        reciproc = 1 / remainder
        n = reciproc
        print(whole, remainder, reciproc)


def contfrac_sqrt(D):
    """Continued fraction representation of sqrt(D).

    This specialisation for the sqrt case uses only integer
    arithmetic (except for the first integer)
    """
    r = 0
    s = 1
    whole = int(math.sqrt(D))

    # Sequentially going from
    # (sqrt(D) + r)/s to a + (sqrt(D)-(a*s-r))/s
    # then reciprocate the fraction and mul
    # by (sqrt(D) + r_new)/(sqrt(D) + r_new)
    # where r_new = a * s - r and continue
    # See
    # https://math.stackexchange.com/a/980515
    # https://math.stackexchange.com/a/4425617
    while True:
        if s == 0:
            break
        a = (r + whole) // s
        r = a * s - r
        s = (D - r * r) // s
        yield a


def convergents(cfrac):
    """Generates successive rational approximations to the value
    given by `cfrac` which is a sequence of continued fraction terms.

    In fact these represent the best possible rational approximations
    in terms of denominator size.

    https://en.wikipedia.org/wiki/Continued_fraction#Infinite_continued_fractions_and_convergents
    """
    h_prev = 1
    h_prev_prev = 0
    k_prev = 0
    k_prev_prev = 1
    for a in cfrac:
        h = a * h_prev + h_prev_prev
        k = a * k_prev + k_prev_prev
        yield Fraction(h, k)
        h_prev_prev = h_prev
        k_prev_prev = k_prev
        h_prev = h
        k_prev = k


def test_convergents():
    # Little check that we can approximate sqrt
    # to the same level of accuracy as math.sqrt
    for D in range(2000):
        if math.sqrt(D) == int(math.sqrt(D)):
            continue
        # Take the 100th convergent
        val = next(islice(convergents(contfrac_sqrt(D)), 100, None))
        assert float(val) == math.sqrt(D)


if __name__ == "__main__":
    test_convergents()

    xs = []
    ds = []

    for D in range(2, 1001):
        if math.sqrt(D) == int(math.sqrt(D)):
            continue

        for conv in convergents(contfrac_sqrt(D)):
            x = conv.numerator
            y = conv.denominator

            if x**2 - D * y**2 == 1:
                print(D, x, y)
                xs.append(x)
                ds.append(D)
                break

    xmax_idx = np.argmax(xs)
    print(f"Maximum x is {xs[xmax_idx]} for D={ds[xmax_idx]}")
