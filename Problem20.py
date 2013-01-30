#!/usr/bin/env python2

# Functions for doing arithmetic based on ASCII values
# so we do not have to rely on Python's arbitrary precision

def add(v1, v2):
    v1 = str(v1)
    v2 = str(v2)
    # Pad with 0s so strings same length
    maxw = max(len(v1),len(v2))
    v1 = v1.rjust(maxw,'0')
    v2 = v2.rjust(maxw,'0')

    c = 0;
    num = "";

    for i in range(maxw-1,-1,-1):
        sumdigits = str(int(v1[i]) + int(v2[i]) + c)

        num = sumdigits[-1] + num
        #print sumdigits, num
        c = int('0' + sumdigits[:-1])
    return (str(c) if c != 0 else '') + num
        

def multiply(v1, v2):
    v1 = str(v1)
    v2 = str(v2)

    nums = []
    for i, digit2 in enumerate(reversed(v2)):
        num = "0" * i
        c = 0
        for digit1 in reversed(v1):
            mul = str(int(digit1) * int(digit2) + c)
            num = mul[-1] + num
            c = int('0' + mul[:-1])
            #print mul
        nums.append((str(c) if c != 0 else '') + num)
    return reduce(add,nums,0)

def fac(n):
    stringnums = map(str,range(n,1,-1))
    return reduce(multiply, stringnums, '1')

def sumdigits(n):
    digits = list(str(n))
    return reduce(add,digits,0)

print sumdigits(fac(100))
    
