import json
import math


def letter2num(c):
    """Return 1-based alphabetical position of a letter"""
    return ord(c.upper()) - ord("A") + 1


def word2nums(w):
    return [letter2num(c) for c in w]


def istriangle(t):
    n = math.floor(math.sqrt(2 * t))
    return (n * (n + 1)) / 2 == t


if __name__ == "__main__":
    with open("./p042_words.txt") as f:
        words = json.loads("[" + f.read() + "]")

    # Little check that this works for factoring
    # triangle numbers
    for i in range(1000000):
        T = (i * (i + 1)) / 2
        assert i == math.floor(math.sqrt(2 * T))

    n_triangle = 0
    for word in words:
        n_triangle += int(istriangle(sum(word2nums(word))))

    print(n_triangle)
