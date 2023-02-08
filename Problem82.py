import numpy as np

example = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331],
]

with open("p082_matrix.txt", "r") as f:
    matrix_string = f.read()
matrix_list = [
    list(map(int, l.split(","))) for l in matrix_string.split() if l.strip() != ""
]

matrix = np.array(matrix_list)
#matrix = np.array(example)

# Use Dijkstra's algorithm

def dijkstra(matrix: np.ndarray, source: tuple[int, int]) -> np.ndarray:
    """Return a distance matrix giving the shortest distances from
    the source index of the input matrix to every other position,
    where the cost is given by the elements of the input matrix and
    only moving up, down, and right
    """
    h, w = matrix.shape
    dists = np.zeros((h, w)) + np.inf
    dists[source] = matrix[source]

    previous_nodes = np.zeros((h, w), dtype=int) - 1

    seen = np.zeros((h, w))

    while seen.min() == 0:
        idx_1d = np.argmin(seen + dists)
        i, j = idx_1d // w, idx_1d % w

        seen[i, j] = np.inf

        # only moving up, down, and right
        for neighbour in ((i-1, j), (i + 1, j), (i, j + 1)):
            try:
                tentative_dist = dists[i, j] + matrix[neighbour]
            except IndexError:
                continue

            if tentative_dist < dists[neighbour]:
                dists[neighbour] = tentative_dist
                previous_nodes[neighbour] = idx_1d
    return dists

overall_min = float("inf")

for source_row in range(0, matrix.shape[0]):
    # Loop through i indexes, trying different sources from 
    # the left column and tracking the smallest distance we
    # get to the rightmost column
    distances = dijkstra(matrix, (source_row, 0))
    min_dist_to_right_column = distances[:,-1].min()

    if min_dist_to_right_column <  overall_min:
        overall_min = min_dist_to_right_column

        print(f"Row {source_row} new min is {overall_min}")
