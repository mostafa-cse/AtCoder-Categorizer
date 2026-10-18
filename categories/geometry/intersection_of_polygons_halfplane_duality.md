# Polygons(2D)

**Taxonomy Path**: `Geometry` > `Geometry 2D` > `Polygons(2D)`

## Description
This topic focuses on polygons(2d) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The intersection of convex polygons is defined by the intersection of all their bounding half-planes. Since the translations only affect the constant term of each half-plane, the intersection of translated copies preserves the normal vectors $A_k, B_k$ and simply tightens the threshold to $\max_i (A_k u_i + B_k v_i)$.
- Common Reductions: Determine whether each query point $(a, b)$ lies inside the intersection of $M$ translated convex $N$-gons $P + (u_i, v_i)$. A point $q \in P + v_i \iff q - v_i \in P$. Each CCW edge of $P$ defines a half-plane $A_k x + B_k y \ge C_k$. Substituting $q - v_i$ yields $A_k a + B_k b \ge C_k + (A_k u_i + B_k v_i)$. Taking the maximum over all $M$ shifts precomputes $M_k = \max_i (A_k u_i + B_k v_i)$, allowing $O(N)$ checks per query.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc251_g`](../../analysis/AtCoder-abc251_g.md) | G. Intersection of Polygons | 2468 | Determine whether each query point $(a, b)$ lies inside the intersection of $M$ translated convex $N$-gons $P + (u_i, v_... |
