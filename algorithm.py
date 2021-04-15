def not_in(element, subset):
    return ((1 << element) & subset) == 0


def combinations(thisSet, at, r, nodes, subsets):
    if r == 0:
        subsets.add(thisSet)
    else:
        for i in range(at, nodes):
            thisSet = thisSet | (1 << i)

            combinations(thisSet, i + 1, r - 1, nodes, subsets)

            thisSet = thisSet & ~(1 << i)


def combinations(r, nodes):
    subsets = []
    combinations(0, 0, r, nodes, subsets)
    return subsets


def min_path(matrix, memo, start, nodes):
    e_state = (1 << nodes) - 1
    min_cost = float('inf')

    for end in range(nodes):
        if end == start:
            continue
        cost = memo[end][e_state] + matrix[end][start]
        if cost < min_cost:
            min_cost = cost
    return min_cost


def optimal_path(matrix, memo, start, nodes):
    last_index = start
    current_state = (1 << nodes) - 1
    path = [0] * (nodes + 1)

    for i in range(nodes, -1, -1):
        index = -1
        for j in range(nodes):
            if j == start | not_in(j, current_state):
                continue
            if index == -1:
                index = j
            prev_dist = memo[index][current_state] + matrix[index][last_index]
            new_dist = memo[j][current_state] + matrix[j][last_index]
            if new_dist < prev_dist:
                index = j
        path[i] = index
        current_state = current_state ^ (1 << index)
        last_index = index

    path[0] = path[nodes] = start
    return path


def setup_memo(matrix, memo, start, nodes):
    for i in range(nodes):
        if i == start:
            continue
        memo[i][1 << start | 1 << i] = matrix[start][i]


def solve(matrix, memo, start, nodes):
    for r in range(3, nodes):
        for subset in combinations(r, nodes):
            if not_in(start, subset):
                continue
            for nextUp in range(nodes):
                if nextUp == start | not_in(nextUp, subset):
                    continue
                current_state = subset ^ (1 << nextUp)
                minimum = float('inf')
                for end in range(nodes):
                    if end == start | end == nextUp | not_in(end, subset):
                        continue
                    new_distance = memo[end][current_state] + matrix[end][nextUp]
                    if new_distance < minimum:
                        minimum = new_distance
                memo[nextUp][subset] = minimum


def tsp_route(matrix, start):
    nodes = matrix.size

    memo = [[0 for x in range(nodes)] for y in range(2 ** nodes)]

    setup_memo(matrix, memo, start, nodes)
    solve(matrix, memo, start, nodes)

    min_p = min_path(matrix, memo, start, nodes)
    route = optimal_path(matrix, memo, start, nodes)

    return min_p, route
