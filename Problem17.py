#!/usr/bin/env python2

units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

tweens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

suffixes = ["hundred", "thousand"]

N = 1000

numbers = []

for n in range(1,N+1):
    s = str(n)
    l = len(s)
    num = ""

    unit = s[-1]
    if l >= 2 and s[-2] == '1':
        num = tweens[int(unit)]
    else:
        num = units[int(unit)]

    if l >= 2 and s[-2] != '1':
        num = tens[int(s[-2])] + num

    if l >= 3:
        if s[-l] != '0':
            andstr = "and" if l==3 and s[-2:] != '00' else ""
            num = units[int(s[-l])] + suffixes[l-3] + andstr + num

    numbers.append(num)

    print n,num
       
print len("".join(numbers)) 
