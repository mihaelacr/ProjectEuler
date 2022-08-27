import numpy as np


def triangles():
    n = 1
    while True:
        yield (n * (n + 1)) // 2
        n += 1


def inverse_pentagonal(p):
    return (0.5 + np.sqrt(0.25 + 6 * p)) / 3.0


def is_pentagonal(p):
    # Will have precision issues if the
    # floats get too large
    return float(inverse_pentagonal(p)).is_integer()


def inverse_hexagonal(h):
    return (1 + np.sqrt(1 + 8 * h)) / 4


def is_hexagonal(h):
    return float(inverse_hexagonal(h)).is_integer()


for t in triangles():
    if is_pentagonal(t) and is_hexagonal(t):
        print(t)
        if t > 40755:
            break
