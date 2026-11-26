# Two trees that refute Bašić’s AG maximizer characterization

**Result.** For every $n=19+5t$, $t\ge0$, there is a tree of order $n$ and maximum degree six whose arithmetic–geometric index exceeds that of **every** tree with the structure prescribed in Corollary 4 of Milan Bašić’s October 25, 2026 preprint. The smallest pair in this construction has 19 vertices. [Bašić, Corollary 4 and Theorem 1](https://arxiv.org/html/2610.34361v1#S2)

## The claim and the two trees

An edge joining vertices of degrees $i,j$ contributes $w_{ij}=(i+j)/(2\sqrt{ij})$ to the arithmetic–geometric index $AG$. Corollary 4 concerns trees of any order with $3\leq\Delta\leq8$. It applies Theorem 1, which specifies only edge types $(1,\Delta),(\Delta,\Delta)$ at $n\equiv2\bmod(\Delta-1)$. At other orders, it specifies one extra vertex of degree $x$, adjacent to $x$ distinct vertices of degree $\Delta$, with $2\leq x<\Delta$ and $n\equiv x+1\bmod(\Delta-1)$. For $\Delta=6$ and $n=19$, this forces $x=3$. [Statement of Theorem 1](https://arxiv.org/html/2610.34361v1#S2.SS1)

* **Predicted tree $T$.** Join a central degree-three vertex to three vertices of degree six. Attach five leaves to each of those three vertices.
* **Competing tree $U$.** Start with a path on three vertices. Subdivide each edge once. Attach five, four and five leaves, respectively, to the three original path vertices, raising all three degrees to six.

Both constructions give connected trees on 19 vertices. Their edge counts give the exact difference below.

| Edge degrees | $T$ | $U$ |
|---|---:|---:|
| $(1,6)$ | 15 | 14 |
| $(2,6)$ | 0 | 4 |
| $(3,6)$ | 3 | 0 |
| $(6,6)$ | 0 | 0 |

$$
AG(U)-AG(T)=4w_{26}-3w_{36}-w_{16}
=\frac{16\sqrt2-9\sqrt3-7}{2\sqrt6}>0 .
$$

Indeed, $16\sqrt2>7+9\sqrt3$ follows by squaring the positive sides twice. The first comparison reduces to $220>126\sqrt3$, and the second is the integer inequality **$48400>47628$**.

## Why this defeats the entire claimed class

At order $19+5t$, the proposed extra degree is still three. If $h$ is the number of degree-six vertices and $l$ the number of leaves, then $l+1+h=n$ and $l+3+6h=2(n-1)$. Hence $h=3+t$ and $l=15+4t$. All leaves attach to degree-six vertices, the one degree-three vertex contributes three $(3,6)$ edges, and the remaining $t$ edges have type $(6,6)$. These multiplicities determine the index of every tree prescribed by the corollary.

To produce both trees at the next order, choose a leaf adjacent to a degree-six vertex and attach five new leaves to it. Its degree becomes six. This adds five vertices, replaces one $(1,6)$ edge by one $(6,6)$ edge, and creates five new $(1,6)$ edges. Both indices therefore increase by $4w_{16}+w_{66}$. The operation leaves eligible leaves for the next iteration and keeps $T$ in the prescribed class. The gap stays strictly positive at every order in the progression. The [classification proof](../classification/proof.md) also establishes that the competitor attains the global maximum throughout this progression. The [complete 19-vertex census](../audits/order19.json) places the predicted tree second.

## Where the argument fails

In Theorem 1’s proof, immediately above equation (16), the author minimizes the unweighted count $\sum_x x n_x$ and concludes that it minimizes the penalty $\sum_x x n_xG(x,\Delta)$ because the weights $G(x,\Delta)$ are positive. Distinct degrees have distinct weights. Here four incidences at degree two cost less than three at degree three, exactly the comparison certified above. Both edge patterns are realizable. [Equations (15)–(16)](https://arxiv.org/html/2610.34361v1#S2.SS1)

**Scope of the hypotheses.** Corollary 4 has only the stated degree and order conditions. Theorem 1 is conditional on properties (P1)–(P5). The paper tests (P4) using an integral upper degree $x<\Delta$, hence $x\leq\Delta-1$. Under this interpretation the AG weight satisfies all five properties at $\Delta=6$.

* (P1) gives $w_{xx}=1$. (P2) follows by strict arithmetic–geometric mean for $x<6$. For (P3), $\partial_y w_{xy}=(y-x)/(4y\sqrt{xy})>0$ when $x<y$.
* In (P4), $C_6=(7\sqrt6-12)/10>1/2$. For $1\le t<x\le5$, multiplying $|\partial_t w_{tx}|$ by $t^2$ gives $\sqrt t(x-t)/(4\sqrt x)\le x/(6\sqrt3)\le5/(6\sqrt3)<1/2$. The first bound follows by maximizing at $t=x/3$ on $[0,x]$.
* For (P5), put $s=\sqrt6$ and $u=\sqrt x$. Its left side is

  $$
  1-w_{x6}+C_6(1/x-1/6)
   =\frac{(s-u)(u-1)((s+1)u-s(s-1))}{2su^2(s+1)}.
  $$

  For $2\le x\le5$ every factor is positive. In particular $s(s-1)/(s+1)<15/14<\sqrt2\le u$, since $s<5/2$ and $s(s-1)/(s+1)$ is increasing for $s>1$.

Under a literal reading allowing **real** $x$ all the way to $\Delta$ in (P4), that hypothesis is incompatible with (P5). For fixed $2\le a\le\Delta-1$ and $a<x<\Delta$, the derivative bound gives $f(1,x)-f(a,x)\le C_\Delta(1-1/a)$. Continuity as $x\uparrow\Delta$, and $f(1,\Delta)=f(\Delta,\Delta)+C_\Delta(1-1/\Delta)$, imply $f(a,\Delta)\ge f(\Delta,\Delta)+C_\Delta(1/a-1/\Delta)$, reversing the strict inequality (P5). The unconditional counterexample to Corollary 4 is independent of this interpretation. [Original conditions and AG specialization](https://arxiv.org/html/2610.34361v1#S2.SS2)

## Prior work and reproducibility

The target is version 1 of Bašić’s *A general algebraic characterization of extremal $\Delta$-trees and $k$-cyclic graphs for degree-homogeneous VDB indices*. His separate October 14 preprint includes AG corollaries for $\Delta=3,4$. The chemical-tree exceptions at orders $6,7,10$ were already explicit in Hertz, Bonte, Devillez, Dusollier, Mélot and Schindl (2024), following their Table 2. That paper studies maximum degree at most four. Searches for the October 25 paper, corrections, and arithmetic–geometric extremal trees of prescribed degree six located no prior source for this particular pair as of November 26, 2026. Priority remains unverified. [Target preprint history](https://arxiv.org/abs/2610.34361) · [October 14 preprint](https://arxiv.org/abs/2610.20364) · [2024 chemical-tree characterization](https://arxiv.org/html/2403.05226v1#S5)

Run **python verify.py** from this directory. The standard-library checker constructs both graphs, checks connectedness and degrees, derives their edge counts, and verifies the radical comparison in integers. It also tests ten successive extensions. The argument above covers every $t\ge0$. [Exact checker](verify.py)
