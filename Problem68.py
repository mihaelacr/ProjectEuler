import itertools

found = set()
found_integers = []

N = 5  # Number of polygon sides
MAX_DIGITS = 16

# Brute force all N! combinations of the variable assignments
num_nodes = 2 * N
for p in itertools.permutations(range(1, num_nodes + 1), num_nodes):
    external_nodes = p[0:N]
    internal_nodes = p[N:]

    # Sum the nodes in each triplet that forms a line, using mod to wrap around
    sums = [
        external_nodes[i] + internal_nodes[i] + internal_nodes[(i + 1) % N]
        for i in range(N)
    ]

    if len(set(sums)) == 1:
        # List of the triplets forming each line
        lines = [
            (external_nodes[i], internal_nodes[i], internal_nodes[(i + 1) % N])
            for i in range(N)
        ]

        # Re-order so that the lowest external node comes first
        lowest_idx = external_nodes.index(min(external_nodes))
        ordered = tuple([lines[l % N] for l in range(lowest_idx, lowest_idx + N)])

        if ordered not in found:
            print(ordered, sum(ordered[0]))
            found.add(ordered)
            flattened = [str(item) for sublist in ordered for item in sublist]
            num_str = "".join(flattened)
            found_integers.append(int(num_str))

print(max([g for g in found_integers if len(str(g)) == MAX_DIGITS]))
