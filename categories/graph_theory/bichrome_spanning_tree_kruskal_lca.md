# Minimum Spanning Tree (MST) - Prim's and Kruskal's

**Taxonomy Path**: `Graph Theory` > `Minimum Spanning Tree (MST)` > `Minimum Spanning Tree (MST) - Prim's and Kruskal's`

## Description
This topic focuses on minimum spanning tree (mst) - prim's and kruskal's techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If $X < W(T_0)$, answer is 0. If $X > W(T_0)$, all $C_<$ edges must have the same color (2 choices) so that no tree with weight $< X$ is bichromatic; then at least one edge of $C_=$ must have the opposite color: $2 \cdot (2^{C_=} - 1) \cdot 2^{C_>}$. If $X = W(T_0)$, $C_< = 0$, and an MST is bichromatic iff $C_=$ is not monochromatic: $(2^{C_=} - 2) \cdot 2^{C_>}$.
- Common Reductions: Color graph edges Black or White ($2^M$ colorings). Count colorings where the minimum weight bichromatic spanning tree has weight exactly $X$. Find an unconstrained MST $T_0$ with weight $W(T_0)$. For each edge $e = (u, v)$, the minimum weight spanning tree containing $e$ has cost $cost(e) = W(T_0) + W(e) - \max\_e$, where $\max\_e$ is the heaviest edge on the tree path between $u$ and $v$ in $T_0$. Count edges with $cost(e) < X$ ($C_<$) and $cost(e) == X$ ($C_=$).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc093_c`](../../analysis/AtCoder-arc093_c.md) | E. Bichrome Spanning Tree | 2551 | Color graph edges Black or White ($2^M$ colorings). Count colorings where the minimum weight bichromatic spanning tree h... |
