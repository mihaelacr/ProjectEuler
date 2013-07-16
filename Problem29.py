#!/usr/bin/env python2

nums = set()

# Find all combinations of a**b
# using set to avoid repeats
for a in range(2,101):
    for b in range(2,101):
        nums.add(a**b)

print len(nums)
