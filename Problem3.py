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


def prime_factorization(number):
    """Return the unique prime factorization of `number`
    (including repeated factors)
    
    cf the Fundamental Theorem of Arithmetic
    """
    factors = []
    running_product = 1
    current_number = number

    # Loop through the primes, iteratively dividing our
    # number by each prime `p` so long as `p` exactly
    # divides `current_number`
    for p in primes():
        while (current_number % p) == 0:
                current_number = current_number // p
                factors.append(p)
                running_product *= p
        if running_product == number:
            return factors

if __name__ == "__main__":
    print(prime_factorization(600851475143))
