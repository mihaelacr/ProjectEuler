for a in range(1, 333):
    for b in range(a + 1, (1000 - a)):
        c = 1000 - a - b

        if b >= c:
            continue

        assert a < b < c

        if a * a + b * b == c * c:
            print(a, b, c)
            print(a * b * c)
