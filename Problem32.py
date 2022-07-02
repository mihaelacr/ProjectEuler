"""
We want to find numbers a*b=c where a|b|c contains
all digits 1..9 once and | represents digit concatenation.

And then sum all unique products c.

I just loop through at-most-four digit numbers
for a and b (which are safe upper bounds since
then c itself would be 8 digits) and use python
string operations to compare digits.
"""

prods = set()

for a in range(9999):
    for b in range(9999):
        c = a * b

        digits_concat = str(a) + str(b) + str(c)

        if "".join(sorted(digits_concat)) == "123456789":
            prods.add(c)
            print(a, b, c, len(prods), sum(prods))

print(sum(prods))
