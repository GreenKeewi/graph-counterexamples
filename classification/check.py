"""Certify the arithmetic–geometric index table using only Python integers."""

from itertools import combinations_with_replacement
from math import isqrt


WINNERS = {
    3: [(), (2,)],
    4: [(), (2,), (3,)],
    5: [(), (2,), (3,), (4,)],
    6: [(), (2,), (2, 2), (4,), (5,)],
    7: [(), (2,), (2, 2), (2, 2, 2), (2, 2, 2, 2), (6,)],
    8: [(2,) * r for r in range(7)],
}

SCALE = 10**12


def radical_bounds(i):
    """Bounds for SCALE times sqrt(i), rounded outwards to integers."""
    square = i * SCALE**2
    lower = isqrt(square)
    return lower, lower if lower**2 == square else lower + 1


def penalty_bounds(d, i):
    """Bounds for SCALE times 2*sqrt(d)*(d-1)*c_i."""
    d_low, d_high = radical_bounds(d)
    i_low, i_high = radical_bounds(i)
    constant = (d - i) * (d + 1) * SCALE
    positive = 2 * d * (i - 1)
    negative = (d - 1) * (d + i)
    return (
        constant + positive * d_low - negative * i_high,
        constant + positive * d_high - negative * i_low,
    )


def certify(d, winners):
    modulus = d - 1
    costs = {i: penalty_bounds(d, i) for i in range(2, d)}
    assert all(low > 0 for low, _ in costs.values())
    assert len(winners) == modulus
    assert all(sum(i - 1 for i in row) == r for r, row in enumerate(winners))
    upper = [sum(costs[i][1] for i in row) for row in winners]
    checked = 0
    for length in range(modulus):
        for row in combinations_with_replacement(range(2, d), length):
            r = sum(i - 1 for i in row) % modulus
            if row != winners[r]:
                assert sum(costs[i][0] for i in row) > upper[r], (d, r, row)
            checked += 1
    return checked


if __name__ == "__main__":
    total = 0
    for degree, winners in WINNERS.items():
        checked = certify(degree, winners)
        total += checked
        print(f"Maximum degree {degree}: {len(winners)} residues, {checked} multisets")
    print(f"Verified 27 residue entries against {total} multisets.")
