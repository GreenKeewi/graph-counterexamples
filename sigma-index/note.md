# A ten-vertex exception to the sigma uniqueness claim

**Scope.** Corollary 6 in Milan Bašić’s October 14 preprint says every maximizing tree uses only edges of types $(1,D)$ and $(2,D)$, where $D$ is its maximum degree. The following example contradicts the exclusivity assertion even at an order where the proposed edge pattern is realizable. The maximum sigma index of chemical trees has an earlier literature. [Corollary 6 and equation (46)](https://arxiv.org/html/2610.20364v1#S4) · [Kovijanić Vukićević et al., 2024](https://doi.org/10.46793/match.91-1.267K) · [Knor, Sedlar and Škrekovski, introduction](https://arxiv.org/html/2608.07402v1#S1)

The sigma index sums $(i-j)^2$ over edges whose endpoint degrees are $i,j$. For a tree with $n\ge4$ and maximum degree three, let $m_{ij}$ count such edges. Then

$$\sigma(T)=2n+4-4m_{12}-2m_{22}.$$

Indeed, subtract $(i-j)^2$ from $6(1/i+1/j)-4$ on each edge. The difference is four for $(1,2)$, two for $(2,2)$ and zero for $(1,3),(2,3),(3,3)$. These are all the possibilities. Summing $1/i+1/j$ over the edges counts each vertex once. The identity and upper bound $\sigma(T)\le 2n+4$ follow.

At $n=10$, start with a path on four vertices and attach respectively two, one, one and two leaves. Its six leaf edges each contribute four, and its three $(3,3)$ edges contribute zero. Hence $\sigma=24$, the maximum, with three edges outside the corollary's prescribed types. For comparison, subdivide both edges of a three-vertex path once and attach two, one and two leaves to its original vertices. This second tree uses only the prescribed types and also scores 24.

Equation (46) in the preprint gives a zero penalty for $(3,3)$ when $D=3$. This permits the tie. More generally, any tree with only degrees one and three attains $2n+4$. A path of $3j+1$ internal vertices completed with leaves to make all internal degrees three gives examples at $n=6j+4$ for every $j\ge1$.

AI-assisted check, 26 November 2026. This note records the discrepancy with the October statement and makes no priority claim.
