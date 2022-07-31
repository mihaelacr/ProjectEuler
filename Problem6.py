import numpy as np

N = 100

# With numpy
x = np.arange(1, N + 1)
r = x.sum() ** 2 - (x**2).sum()
print(r)

# Or in closed form
rc = ((N * (N + 1)) // 2) ** 2 - (N * (N + 1) * (2 * N + 1)) // 6
assert rc == r
