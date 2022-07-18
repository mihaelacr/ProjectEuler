import math
from fractions import Fraction
from itertools import islice


def contfrac_e():
    """The continued fraction expansion of e as a generator"""

    yield 2

    k = 1
    while True:
        yield 1
        yield 2 * k
        yield 1
        k += 1


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


def test_e_is_e():
    # Check we can reach the same accuracy as
    # python's floating point math.e
    val = next(islice(convergents(contfrac_e()), 100, None))
    assert float(val) == math.e


if __name__ == "__main__":
    test_e_is_e()

    numerator_10th = next(islice(convergents(contfrac_e()), 10 - 1, None)).numerator
    assert sum(map(int, str(numerator_10th))) == 17

    numerator_100th = next(islice(convergents(contfrac_e()), 100 - 1, None)).numerator
    numerator_100th_digitsum = sum(map(int, str(numerator_100th)))
    print(
        f"Sum of digits of numerator of 100th convergent of e is {numerator_100th_digitsum}"
    )
