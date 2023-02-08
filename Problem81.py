import numpy as np

example = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331],
]

with open("p081_matrix.txt", "r") as f:
    matrix_string = f.read()
matrix_list = [
    list(map(int, l.split(","))) for l in matrix_string.split() if l.strip() != ""
]

matrix = np.array(matrix_list)
#matrix = np.array(example)
h, w = matrix.shape

# Use Dijkstra's algorithm

# Current shortest distance to source
dists = np.zeros((h, w)) + np.inf
dists[0, 0] = matrix[0, 0]

previous_nodes = np.zeros((h, w), dtype=int) - 1

seen = np.zeros((h, w))

while seen.min() == 0:
    idx_1d = np.argmin(seen + dists)
    i, j = idx_1d // w, idx_1d % w

    seen[i, j] = np.inf

    for neighbour in ((i + 1, j), (i, j + 1)):
        try:
            tentative_dist = dists[i, j] + matrix[neighbour]
        except IndexError:
            continue

        if tentative_dist < dists[neighbour]:
            dists[neighbour] = tentative_dist
            previous_nodes[neighbour] = idx_1d

route = []
def follow_prevs(n):
    if n != -1:
        route.append(matrix.reshape(-1)[n])
        follow_prevs(previous_nodes.reshape(-1)[n])

follow_prevs(matrix.size - 1)

print("Distances from each node to source (top left)")
print(dists)

print("Min dist from bottom right to source", dists[-1,-1])

print("Route")
print(route)
