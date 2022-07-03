from fractions import Fraction
from math import prod


def cancel_digits(numerator, denominator):
    """
    Cancel out the common digits in numerator and denominator,
    except for the trivial case of cancelling zeros.

    Assuming at most two digit numbers, so there
    is a unique cancelling.
    """
    numer_digits = list(str(numerator))
    denom_digits = list(str(denominator))

    # Treat as an array of strings and iterate
    # through pairs of digits, cancelling inplace
    # by replacing the digits with the empty string
    for i in range(len(numer_digits)):
        for j in range(len(denom_digits)):
            if numer_digits[i] == denom_digits[j]:
                if numer_digits[i] == "0":
                    # Ignore trivial cases
                    continue
                numer_digits[i] = ""
                denom_digits[j] = ""

    # Rebuild the number into an integer, using 0
    # as a sentinel if a number got completely
    # cancelled
    numer_int = int("0" + "".join(numer_digits))
    denom_int = int("0" + "".join(denom_digits))

    return numer_int, denom_int


curious_fractions = []

for d in range(1, 100):
    for n in range(1, d):  # Up to d since fraction < 1
        nc, dc = cancel_digits(n, d)

        f_orig = Fraction(n, d)
        f_cancelled = Fraction(nc, dc) if dc != 0 else None

        if f_orig == f_cancelled and (n, d) != (nc, dc):
            print(f"{n}/{d} -> {nc}/{dc}")
            curious_fractions.append(f_orig)

curious_product = prod(curious_fractions)
print("Curious product:", curious_product, "Denominator:", curious_product.denominator)
