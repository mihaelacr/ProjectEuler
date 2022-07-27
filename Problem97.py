# Slow way thanks to Python's support
# for gigantic ints
# print(str(28433 * 2**7830457 + 1)[-10:])

# Quick way with modpow
# Use mod 10**10 to get last 10 digits
print((28433 * pow(2, 7830457, mod=10**10) + 1) % 10**10)
