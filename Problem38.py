import itertools

# Define "concatenated product" * between
# an integer and a sequential tuple of digits as
# y = x * (1,2,...n) = x | 2x | ... | nx
# where | is digit concatenation
# and we want to find the largest y
# that is 1-to-9 pandigital (assume n>1)

def tuple2int(t):
    return int("".join(map(str, t)))


def check_multiples(x, tail, multiple):
    """Recursively check if the digits of the 
    `tail` tuple match incremental multiples of `x`,
    consuming the matching number of digits from the
    beginning of the tuple and increasing
    `multiple` by 1 at each recursion.
    """
    if len(tail) == 0:
        # Base case where we have reached an empty tuple
        # so it is a successful match
        return True

    digit_mul = x * multiple
    nd = len(str(digit_mul))

    # Check if the next `nd` digits in the tuple
    # are indeed the expected multiple of x
    if tuple2int(tail[:nd]) == digit_mul:
        return check_multiples(x, tail[nd:], multiple + 1)
    else:
        return False


results = []

#for p in itertools.permutations(range(1, 10), 9):
# Or if we only check those starting with 9 (max 8! = 40320 digits left to check):
for p in ((9,) + s for s in itertools.permutations(range(1, 9), 8)):
    # Loop through different chunkings of the digits
    # corresponding to different choices of initial x
    for n_digits in range(1, 5):
        first_chunk = p[0:n_digits]

        if check_multiples(tuple2int(first_chunk), p[n_digits:], 2):
            print(f"{first_chunk=}, pandigital={p}")
            results.append(tuple2int(p))

print(f"Largest is {max(results)}")
