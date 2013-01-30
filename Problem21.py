#!/usr/bin/env python2

import math

N = 10000

# Inefficiently factorise an integer
def factors(n):
    if n == 1:
         return [1]

    factors = [x for x in range(1,int(math.ceil(n**0.5)+1)) if n % x == 0]

    factors += [n/k for k in factors]

    # exclude number itself
    factors.remove(n)

    return list(set(factors))

# Compute factor sums
d = [0] * (N+1)

for n in range(1,N+1):
    d[n] = sum(factors(n))

amicable = []

# Find the amicable numbers
for a in range(1,N+1):
    b = d[a]
    if a != b and b<=10000 and a == d[b] and a not in amicable:
        amicable += [a,b]


print sum(amicable)
