palindromes = []

n_digits = 3
range_begin = 10 ** (n_digits - 1)
range_end = 10 ** (n_digits)

for i in range(range_begin, range_end):
    for j in range(range_begin, range_end):
        if j > i:
            # Since multiplication is commutative
            break
        p = i * j
        p_str = str(p)
        if p_str == p_str[::-1]:
            palindromes.append(p)

print(max(palindromes))
