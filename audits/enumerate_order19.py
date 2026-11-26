"""Independently enumerate all 19-vertex unlabeled trees with NetworkX.

Run: python enumerate_order19.py order19.json
"""

import argparse
from collections import Counter
from fractions import Fraction
from math import isqrt
import json
from pathlib import Path

import networkx as nx


ORDER = 19
DEGREE = 6
PAIRS = [(i, j) for i in range(1, DEGREE + 1) for j in range(i, DEGREE + 1)]
PAIR_INDEX = {pair: i for i, pair in enumerate(PAIRS)}


def radical_key(signature):
    """Exact coefficients of the distinct squarefree radicals."""
    coeff = Counter()
    for (a, b), count in zip(PAIRS, signature):
        if count == 0:
            continue
        product = a * b
        square_root = max(i for i in range(1, isqrt(product) + 1) if product % (i*i) == 0)
        radical = product // (square_root * square_root)
        coeff[radical] += Fraction(count * (a + b) * square_root, 2 * product)
    return tuple(sorted(coeff.items()))


def brackets(signatures, scale):
    # floor(scale * (a+b)/(2*sqrt(ab))) is the integer square root below.
    # Adding one for each edge gives a rigorous strict upper bound.
    lower_weights = [isqrt((scale * (a + b))**2 // (4*a*b)) for a, b in PAIRS]
    return {sig: sum(c*w for c, w in zip(sig, lower_weights)) for sig in signatures}


def top_group(signatures, scale):
    while True:
        lows = brackets(signatures, scale)
        first = max(signatures, key=lows.__getitem__)
        near = [sig for sig in signatures if lows[sig] + ORDER - 1 > lows[first]]
        key = radical_key(first)
        if all(radical_key(sig) == key for sig in near):
            return near, scale, lows
        scale *= 10


def group_record(group, scale, lows, frequencies):
    return {
        "classes": sum(frequencies[sig] for sig in group),
        "signatures": [
            {"classes": frequencies[sig],
             "edgeCounts": {f"{i},{j}": count for (i, j), count in zip(PAIRS, sig) if count}}
            for sig in group
        ],
        "score": {f"sqrt({r})": str(value) for r, value in radical_key(group[0])},
        "scale": str(scale),
        "lowerNumerator": str(max(lows[sig] for sig in group)),
        "strictUpperNumerator": str(min(lows[sig] + ORDER - 1 for sig in group)),
    }


def main(output):
    frequencies = Counter()
    total = 0
    for tree in nx.nonisomorphic_trees(ORDER):
        total += 1
        degrees = dict(tree.degree)
        if max(degrees.values()) != DEGREE:
            continue
        signature = [0] * len(PAIRS)
        for u, v in tree.edges:
            a, b = degrees[u], degrees[v]
            if a > b:
                a, b = b, a
            signature[PAIR_INDEX[a, b]] += 1
        frequencies[tuple(signature)] += 1
    assert total == 317955  # Number of 19-vertex unlabeled trees, A000055.
    maximum, scale, lows = top_group(frequencies, 10**18)
    other = set(frequencies).difference(maximum)
    runner, runner_scale, runner_lows = top_group(other, scale)
    report = {
        "order": ORDER, "maxDegree": DEGREE, "generator": "networkx.nonisomorphic_trees",
        "networkx": nx.__version__, "allTrees": total, "eligibleTrees": sum(frequencies.values()),
        "distinctEligibleEdgeSignatures": len(frequencies),
        "maximum": group_record(maximum, scale, lows, frequencies),
        "runnerUp": group_record(runner, runner_scale, runner_lows, frequencies),
    }
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    main(parser.parse_args().output)
