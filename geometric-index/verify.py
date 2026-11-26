"""Replay the two AG trees and ten extensions, using only exact integer/rational arithmetic."""

from collections import Counter
from fractions import Fraction
from math import isqrt


def make_pair():
    predicted = [(0, 1), (0, 2), (0, 3)]
    competitor = [(0, 3), (3, 1), (1, 4), (4, 2)]
    for edges, first_leaf, attachments in [
        (predicted, 4, [(1, 5), (2, 5), (3, 5)]),
        (competitor, 5, [(0, 5), (1, 4), (2, 5)]),
    ]:
        next_leaf = first_leaf
        for hub, count in attachments:
            for _ in range(count):
                edges.append((hub, next_leaf))
                next_leaf += 1
    return predicted, competitor


def inspect_tree(edges, n):
    neighbours = [set() for _ in range(n)]
    for u, v in edges:
        assert 0 <= u < n and 0 <= v < n and u != v and v not in neighbours[u]
        neighbours[u].add(v)
        neighbours[v].add(u)
    assert len(edges) == n - 1
    seen = {0}
    stack = [0]
    while stack:
        new = neighbours[stack.pop()] - seen
        seen.update(new)
        stack.extend(new)
    assert len(seen) == n
    degrees = list(map(len, neighbours))
    assert max(degrees) == 6
    counts = Counter(tuple(sorted((degrees[u], degrees[v]))) for u, v in edges)
    return degrees, counts


def scaled_index(counts):
    """Represent 2 sqrt(6) AG by a map from square-free radicands to coefficients."""
    result = Counter()
    for (i, j), number in counts.items():
        radicand = 6*i*j
        square_root = next(k for k in range(isqrt(radicand), 0, -1) if radicand % (k*k) == 0)
        result[radicand // (square_root * square_root)] += Fraction(
            number * (i+j) * square_root, i*j
        )
    return result


def extend(edges, degrees):
    # The constructions orient every pendant edge from its neighbour to the leaf.
    leaf = next(v for u, v in edges if degrees[v] == 1 and degrees[u] == 6)
    n = len(degrees)
    edges.extend((leaf, v) for v in range(n, n+5))


def verify():
    predicted, competitor = make_pair()
    for t in range(11):
        n = 19 + 5*t
        p_degrees, p_counts = inspect_tree(predicted, n)
        u_degrees, u_counts = inspect_tree(competitor, n)
        assert p_counts == Counter({(1, 6): 15 + 4*t, (3, 6): 3, (6, 6): t})
        assert u_counts == Counter({(1, 6): 14 + 4*t, (2, 6): 4, (6, 6): t})
        difference = scaled_index(u_counts)
        difference.subtract(scaled_index(p_counts))
        nonzero = {key: value for key, value in difference.items() if value}
        assert nonzero == {1: -7, 2: 16, 3: -9}
        if t < 10:
            extend(predicted, p_degrees)
            extend(competitor, u_degrees)
    # Prove 16 sqrt(2) > 7 + 9 sqrt(3) by two squarings of positive sides.
    lhs = 2*16**2 - 7**2 - 3*9**2
    rhs_coefficient = 2*7*9
    assert lhs > 0 and lhs**2 == 48400 > 47628 == 3 * rhs_coefficient**2
    print("Verified the 19-vertex pair and ten extensions through 69 vertices.")
    print("In each pair, 2 sqrt(6) times the AG improvement is 16 sqrt(2) - 9 sqrt(3) - 7 > 0.")


if __name__ == "__main__":
    verify()
