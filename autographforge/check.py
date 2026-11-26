"""Exact checks for two conjectures from the AutoGraphForge candidate list."""

from collections import deque
from itertools import combinations


def adjacency(order, edges):
    neighbors = [set() for _ in range(order)]
    for left, right in edges:
        if not (0 <= left < order and 0 <= right < order):
            raise ValueError("edge endpoint outside graph")
        if left == right or right in neighbors[left]:
            raise ValueError("graph is not simple")
        neighbors[left].add(right)
        neighbors[right].add(left)
    return neighbors


def path_with_common_neighbors(path_order):
    edges = [(i, i + 1) for i in range(path_order - 1)]
    order = 2 * path_order - 6
    for vertex in range(path_order, order):
        edges.extend([(4, vertex), (5, vertex)])
    return adjacency(order, edges)


def paired_leaf_tree(branch_count):
    edges = []
    for branch in range(branch_count):
        support = 1 + 3 * branch
        edges.extend([(0, support), (support, support + 1), (support, support + 2)])
    return adjacency(1 + 3 * branch_count, edges)


def distances(neighbors, source):
    result = {source: 0}
    queue = deque([source])
    while queue:
        vertex = queue.popleft()
        for other in neighbors[vertex]:
            if other not in result:
                result[other] = result[vertex] + 1
                queue.append(other)
    return result


def slater_number(neighbors):
    degrees = sorted(map(len, neighbors), reverse=True)
    total = 0
    for count, degree in enumerate(degrees, 1):
        total += degree
        if count + total >= len(degrees):
            return count
    raise AssertionError("unreachable on a nonempty graph")


def burn_step(neighbors, burned, source):
    if source in burned:
        raise ValueError("source already burned")
    spread = burned.union(*(neighbors[vertex] for vertex in burned))
    return spread | {source}


def burning_number(neighbors):
    vertices = frozenset(range(len(neighbors)))
    frontier = {frozenset()}
    for round_number in range(1, len(vertices) + 1):
        next_frontier = set()
        for burned in frontier:
            for source in vertices - burned:
                after = burn_step(neighbors, burned, source)
                if after == vertices:
                    return round_number
                next_frontier.add(after)
        frontier = next_frontier
    raise AssertionError("every graph has a burning schedule")


def power_dominates(neighbors, seeds):
    observed = set(seeds).union(*(neighbors[vertex] for vertex in seeds))
    while len(observed) < len(neighbors):
        forced = set()
        for vertex in observed:
            missing = neighbors[vertex] - observed
            if len(missing) == 1:
                forced.update(missing)
        if not forced:
            return False
        observed.update(forced)
    return True


def power_domination_number(neighbors):
    for count in range(1, len(neighbors) + 1):
        for seeds in combinations(range(len(neighbors)), count):
            if power_dominates(neighbors, seeds):
                return count
    raise AssertionError("all vertices together power dominate")


def main():
    path_graph = path_with_common_neighbors(10)
    assert sum(map(len, path_graph)) == 34
    for left in range(10):
        row = distances(path_graph, left)
        assert len(row) == len(path_graph)
        assert all(row[right] == abs(left - right) for right in range(10))
    slater = slater_number(path_graph)
    path_burning = burning_number(path_graph)
    assert (slater, path_burning) == (2, 4)
    burned = frozenset()
    for source in [4, 8, 1, 0]:
        burned = burn_step(path_graph, burned, source)
    assert len(burned) == len(path_graph)

    tree = paired_leaf_tree(5)
    assert sum(map(len, tree)) == 2 * (len(tree) - 1)
    assert len(distances(tree, 0)) == len(tree)
    tree_burning = burning_number(tree)
    power_domination = power_domination_number(tree)
    assert (power_domination, tree_burning) == (5, 3)
    print(f"14-vertex graph: Slater = {slater}, burning = {path_burning}")
    print(f"16-vertex tree: power domination = {power_domination}, burning = {tree_burning}")


if __name__ == "__main__":
    main()
