#!/usr/bin/env python2

numstring = open("/tmp/nums").read()

# Assuming 50 digit numbers (could make more flexible)
NCHUNKS = 5

nums = numstring.split()

# Split into chunks of 10 digits each
groups = [[x[-10*(k+1):len(x)-10*(k)] for x in nums] for k in range(NCHUNKS)]

s=""
c=0

for x in range(len(groups)):
    tot = sum(map(int,groups[x])) + c
    c = tot/10**10
    s = str(tot)[-10:] + s
 
res = str(c) + s

print res

# Verify with python's Long precision
print str(sum(map(int,nums))) == res
