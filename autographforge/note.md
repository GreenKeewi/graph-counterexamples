# Two graph burning inequalities from AutoGraphForge fail by unbounded amounts

Ján Pastorek's *AutoGraphForge: Towards Automated Graph Theory Discovery* reports 6,522 candidate graph statements that survived its computational search. Two of the candidates compare the burning number with the Slater number and the power domination number. We give counterexamples on 14 and 16 vertices. In each case the predicted upper bound can be held constant while the quantity it bounds grows arbitrarily large. [Conference paper, §§4.1–5](https://ceur-ws.org/Vol-4323/paper32.pdf) · [Preprint](https://arxiv.org/html/2609.03478v1#S4.SS2)

Both statements appear in the paper's accompanying list. The hypothesis of each is that the graph is connected and nontrivial. The list assigns touch counts of 2,860 and 1,482, respectively. These statements have the status of research candidates. The paper's proved inequalities (1) and (2) concern edge covers. This note makes no claim of priority. [Slater candidate](https://github.com/JanPastorek/AutoGraphForge/blob/4d1a8afc99447cacd2328cca20e47b6493e8dbc5/results/survivors_by_touch.txt#L22-L23) · [Power domination candidate](https://github.com/JanPastorek/AutoGraphForge/blob/4d1a8afc99447cacd2328cca20e47b6493e8dbc5/results/survivors_by_touch.txt#L60-L61)

## 1. Burning number at fixed Slater number

The first candidate asserts $b(G)\le s(G)+1$. The **burning number** $b(G)$ is the minimum number of rounds needed to burn the graph when one vertex is ignited per round and existing fires spread one edge per round. With degrees $d_1\ge\cdots\ge d_n$, the **Slater number** $s(G)$ is the least $k$ for which $k+\sum_{i=1}^k d_i\ge n$.

**Counterexample.** Take a path $v_0,v_1,\ldots,v_9$. Add four new vertices, each adjacent exactly to $v_4$ and $v_5$. The resulting graph has 14 vertices and 17 edges. The two central vertices have degree 6 and the remaining degrees are at most 2. Thus $1+6<14$ and $2+6+6=14$, giving $s(G)=2$.

The original ten-vertex path remains isometric. Any detour through a new vertex either returns to its starting vertex or goes between $v_4$ and $v_5$, which are already adjacent. A radius-$r$ ball anywhere in the graph therefore covers at most $2r+1$ vertices of this path. Indeed, any two path vertices in the ball are at distance at most $2r$ along the path. Three rounds give fires of final radii $2,1,0$, covering at most $5+3+1=9$ path vertices. Four rounds suffice by successively igniting $v_4,v_8,v_1,v_0$. Thus

$$
b(G)=4>3=s(G)+1 .
$$

**Unbounded gap.** For each $p\ge10$, start with a $p$-vertex path and add $p-6$ common neighbors of the same adjacent internal vertices $v_4,v_5$. The order is $2p-6$ and the two largest degrees are $p-4$, again giving $s(G)=2$. The same isometric path argument yields $b(G)\ge\lceil\sqrt p\rceil$, because $k$ fires cover at most $\sum_{j=0}^{k-1}(2j+1)=k^2$ path vertices. All these graphs are planar and chordal. The central edge and the two-edge paths through its common neighbors admit a planar drawing. Every cycle longer than a triangle is a four-cycle with the central edge as a chord. Planarity and chordality are additional features of the witnesses.

## 2. Power domination at fixed burning number

The second candidate asserts $\gamma_P(G)\le3b(G)-5$. A set of seeds **power dominates** a graph if, after initially observing the seeds and all their neighbors, the following rule observes every vertex. An observed vertex with exactly one unobserved neighbor observes that neighbor. The power domination number $\gamma_P(G)$ is the least number of seeds.

Take a tree with a hub, $t$ neighbors of the hub, and two private leaves on each of those neighbors. The order is $1+3t$. For $t\ge3$, its burning number is exactly 3. A first fire at the hub reaches every vertex within two spreading steps. In two rounds the first fire reaches only its closed neighborhood, which has at most $t+1$ vertices, and the second fire adds at most one. Since $t+2<1+3t$, two rounds cannot suffice.

Each branch requires one seed among its support vertex and its two leaves. If a branch has no seed, its two leaves are initially unobserved. Only their common neighbor could observe the first of them, but it has at least two unobserved neighbors for as long as both leaves remain unobserved. Conversely, choosing every support vertex initially observes the entire tree. Hence $\gamma_P(G)=t$. At $t=5$ this gives a 16-vertex tree satisfying

$$
\gamma_P(G)=5>4=3b(G)-5 .
$$

As $t$ increases, the burning number stays at 3.

## Reproduction

Run [check.py](check.py) with Python 3.10 or later. It builds both graphs, checks the path distances in the first graph, computes the Slater number from the degrees, explores every possible burned set until it finds the exact burning number, and searches seed sets for the exact power domination number in the second graph. The infinite-family claims follow from the arguments above.
