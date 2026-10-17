# Gaussian Elimination Modulo 2

**Taxonomy Path**: `Math` > `Linear Algebra` > `Gaussian Elimination Modulo 2`

## Description
This topic focuses on gaussian elimination modulo 2 techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In any bipartite graph with adjacency matrix $S$, the number of cycle covers modulo 2 equals the determinant of $S$ over $\mathbb{F}_2$. A valid set of cycles with odd total ways exists if and only if $\det(S) \equiv 1 \pmod 2$.
- Common Reductions: Given a bipartite graph with adjacency matrix $S$, determine whether the number of edge subsets where every vertex has an odd degree (or cycle partitions) is odd or even.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc054_c`](../../analysis/AtCoder-arc054_c.md) | C. Carnival | 2292 | Given a bipartite graph with adjacency matrix $S$, determine whether the number of edge subsets where every vertex has a... |
