#!/usr/bin/env python2

# Sides grow 1,3,5,7...
# Circumference grows 1,8,16,24... (s*4-4)

N=1001

sides = [s for s in range(1,N+1) if s % 2 == 1]
circumferences = [max(s*4-4,1) for s in sides]

# Top right value of each concentric rectangle
toprights = circumferences[:]
for i in range(1,len(circumferences)):
    toprights[i] += toprights[i-1]


# Sum the corners of each rectangle
total = 1
for i,v in enumerate(toprights,0):
    diff = sides[i]-1
    for x in [0,1,2,3]:
        total += v-diff*x if i > 0 else 0

print total
