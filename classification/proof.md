# Which trees maximize the arithmetic–geometric index?

AI-assisted research note · 26 November 2026

The 19-vertex competitor in our [counterexample](../geometric-index/) is a global maximizer. The following result also identifies every maximizer for each maximum degree from three through eight once an explicit size condition holds. The degree-three and degree-four cases overlap established results for chemical trees. [Bašić, Corollary 4](https://arxiv.org/html/2610.34361v1#S2.SS2) · [Hertz et al., Section 5](https://arxiv.org/html/2403.05226v1#S5)

## Statement

Let $D$ be the prescribed maximum degree, $3\le D\le8$, and let $r$ be the remainder of $n-2$ modulo $D-1$. Assume $n\ge D(r+1)+1$. A tree on $n$ vertices of maximum degree $D$ maximizes the arithmetic–geometric index exactly when

1. every edge has at least one endpoint of degree $D$, and
2. its multiset of degrees strictly between $1$ and $D$ is the entry below.

A dash denotes the empty multiset and a blank denotes an inapplicable residue. Repeated entries count distinct vertices.

| $D$ | $r=0$ | $r=1$ | $r=2$ | $r=3$ | $r=4$ | $r=5$ | $r=6$ |
|---|---|---|---|---|---|---|---|
| 3 | — | 2 | | | | | |
| 4 | — | 2 | 3 | | | | |
| 5 | — | 2 | 3 | 4 | | | |
| 6 | — | 2 | 2, 2 | 4 | 5 | | |
| 7 | — | 2 | 2, 2 | 2, 2, 2 | 2, 2, 2, 2 | 6 | |
| 8 | — | 2 | 2, 2 | 2, 2, 2 | 2, 2, 2, 2 | 2, 2, 2, 2, 2 | 2, 2, 2, 2, 2, 2 |

For $D=6,r=2$, the size condition is $n\ge19$. At $n=19$ there are precisely three degree-six vertices and two degree-two vertices. All four edges from the degree-two vertices go to degree-six vertices. The internal tree must therefore be a path alternating between those two degrees. The 19-vertex maximizer is unique up to relabeling.

## Proof

Write $f(i,j)=(i+j)/(2\sqrt{ij})$, $f_i=f(i,D)$, and $n_i$ for the number of vertices of degree $i$. For $i\le j\le D$, the quantity $f(i,j)$ increases with $j$ and $f(j,D)\ge1$. Hence

$$f(i,j)\le f_i+f_j-1.$$

Equality holds exactly when $j=D$. Summing over the $n-1$ edges gives an upper bound $\sum_i i n_i f_i-(n-1)$. A tree satisfies $\sum_{i=2}^D(i-1)n_i=n-2$ by the degree-sum identity. Eliminating the leaf and degree-$D$ counts gives

$$AG(T)\le n f_1-(n-1)+(n-2)\frac{D-f_1}{D-1}-\sum_{i=2}^{D-1} c_i n_i,$$

where

$$c_i=(i-1)\frac{D-f_1}{D-1}-i f_i+f_1.$$

It suffices to minimize the final sum under the congruence $\sum_{i=2}^{D-1}(i-1)n_i\equiv r\pmod{D-1}$, then realize the minimizing multiset with equality on every edge.

**Finite arithmetic.** For each $D$ under consideration, every $c_i$ is positive. A minimum-cost multiset has at most $D-2$ entries. Indeed, order the entries arbitrarily and form partial sums of $i-1$, including zero. A word with $D-1$ entries or more repeats a partial-sum residue, and deleting the intervening entries preserves the target residue while reducing cost. The [integer certificate](check.py) verifies positivity and the unique minimizing multiset in each table entry. It visits all 1,274 multisets up to this length across the six values of $D$.

For clarity, the only algebraic comparisons the certificate needs are sums of

$$2\sqrt D(D-1)c_i=(D-i)(D+1)+2D(i-1)\sqrt D-(D-1)(D+i)\sqrt i.$$

For each square root $\sqrt k$ it encloses $10^{12}\sqrt k$ between its integer square root $\lfloor\sqrt{10^{24}k}\rfloor$ and its ceiling, retaining equality at perfect squares. In every comparison between a table entry and a different multiset of the same residue, the entry's upper bound is strictly below the competitor's lower bound. These integer inequalities certify the exact radical comparisons.

**Realizing the bound.** For each winning multiset the ordinary sum of $i-1$ is exactly $r$. Consequently $h=(n-2-r)/(D-1)$ is the required number of degree-$D$ vertices, which we call hubs. The size assumption gives $h\ge r+1$. Start with one hub. For each entry $i$, attach a new vertex of degree $i$ to that same hub and connect it to $i-1$ fresh hubs. There are now $1+r$ hubs. If more are needed, attach them as a path starting at the original hub. The degree of that hub so far is at most $r+1\le D-1$. Attach enough leaves to each hub to bring its degree to $D$. The graph is a tree. Every edge meets a hub, and the degree-sum identity gives exactly $n$ vertices. It attains the upper bound. Any maximizer must attain both the minimum cost and equality on every edge, which gives the characterization. $\square$

The same size condition is necessary to attain this particular bound. Removing leaves from any tree with the two stated properties leaves $h$ hubs and the intermediate vertices. Counting edges in this core gives exactly $h-1-r$ edges between hubs. Smaller orders require a different analysis.

## Scope and reproducibility

This proof covers trees with prescribed *exact* maximum degree in the stated range. It identifies the optimizing degree patterns at every residue within the size condition, including the rows where the preprint's single-intermediate-vertex prediction holds. The formula for the maximum follows by substituting the winning multiset in the displayed upper bound. The argument uses a finite integer certificate for the table and a general construction for all qualifying sizes.

Run the checker with standard Python 3 and assertions enabled.

~~~sh
python classification/check.py
~~~

OpenAI Codex assisted in deriving the result, writing the proofs and checking the arithmetic. The results have not undergone independent human peer review. The prior-art search is recorded in the [counterexample note](../geometric-index/).
