# Cartesian Tree

**Taxonomy Path**: `Data Structures (DS)` > `More Tree Data Structures` > `Cartesian Tree`

## Description
This topic focuses on cartesian tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Fix the bottommost row $d$ and maintain the consecutive vertical heights $h_j$ of dots for each column. On the array $h$, build a Cartesian Tree in $O(M)$ time. Each Cartesian tree node $i$ defines a maximal horizontal interval $[l_i, r_i]$ where $h_i$ is the minimum height. For width $w$, the maximum allowed height is $\min(h_i, \lfloor K / w \rfloor)$. Using precomputed prefix sums over $w$, the contribution of each node is evaluated in $O(1)$ time.
- Common Reductions: Count the number of all-dot sub-rectangles in an $N \times M$ grid that contain at most $K$ cells.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc420_f`](../../analysis/AtCoder-abc420_f.md) | F - kirinuki | 2420 | Count the number of all-dot sub-rectangles in an $N \times M$ grid that contain at most $K$ cells.... |
