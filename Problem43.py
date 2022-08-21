import itertools

primes = [2, 3, 5, 7, 11, 13, 17]


def recursive_digit_prime_divisibility(digits: tuple, unused_digits: set):
    # Recursively check the divisibility by successive primes
    # of the last three digits as we build up the 0-9 pandigital
    # number

    assert len(digits) >= 4

    if len(digits) == 10:
        return [digits]

    # We can find the current prime from the length
    # of the digits so far - we start with d1234 and
    # need to find d345 divisible by primes[1]
    p = primes[len(digits) - 3]

    results = []

    d1 = digits[-2]
    d2 = digits[-1]
    for d3 in unused_digits:
        num = 100 * d1 + 10 * d2 + d3

        if (num % p) == 0:
            next_unused = unused_digits - {d3}
            next_digits = digits + (d3,)
            results += recursive_digit_prime_divisibility(next_digits, next_unused)

    return results


if __name__ == "__main__":

    # We will explicitly handle the first 4 digits
    # and then it's just a moving window we can handle
    # recursively

    all_found = []

    # Can have any digit except 0 for d1
    for d1 in range(1, 10):
        vals = set(range(10)) - {d1}

        # Find the valid even 3-digit numbers for d2 to d4
        for d234 in filter(lambda x: x[-1] % 2 == 0, itertools.permutations(vals, 3)):
            all_found += recursive_digit_prime_divisibility((d1,) + d234, vals - set(d234))

    print(sum([int("".join([str(d) for d in r])) for r in all_found]))
