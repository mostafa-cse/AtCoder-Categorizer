# Tree Diameter

**Taxonomy Path**: `Graph Theory` > `Graph Traversal` > `Tree Diameter`

## Description
This topic focuses on tree diameter techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Let u, v be endpoints of a tree diameter of length D. If u and v have the same color, niceness is always D (2^(N-1) colorings). If u and v have different colors (say u White, v Black), for any threshold d, a vertex w can be freely colored if max(d_u(w), d_v(w)) <= d. If min(d_u(w), d_v(w)) > d, 0 colorings exist. Otherwise, its color is forced. Thus, the number of colorings with niceness <= d is 2 * 2^{free(d)} for d >= max_w min(d_u(w), d_v(w)).
- Common Reductions: Given a tree of N vertices, paint each vertex Black or White. Niceness is the maximum distance between vertices of the same color. Compute the sum of nicenesses over all 2^N colorings modulo 10^9 + 7.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc108_f`](../../analysis/AtCoder-arc108_f.md) | F - Paint Tree | 2646 | Given a tree of N vertices, paint each vertex Black or White. Niceness is the maximum distance between vertices of the s... |
