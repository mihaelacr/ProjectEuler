#!/usr/bin/env python2

nums = []

# Maximum determined by the
# "eh, should be enough" method
for i in range(2,1000000):
    digits = map(int, str(i))
    sumpow = sum([x**5 for x in digits])
    if i == sumpow:
        nums.append(i)

print sum(nums)
