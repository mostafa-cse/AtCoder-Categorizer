# 2D Prefix Sum

**Taxonomy Path**: `Basics` > `2D Prefix Sum` > `2D Prefix Sum`

## Description
This topic focuses on 2d prefix sum techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The region covered by a piece at $(s, t)$ is a right triangle where on each row $u \in [s, s + M - 1]$, the covered columns form an interval $[t, t + 2M - 1 - 2(u - s)]$. The start boundary is vertical (constant $t$), while the end boundary is a diagonal with direction $(\Delta u = 1, \Delta v = -2)$.
- Common Reductions: Count how many pieces cover each query square in a scalene triangle region. Triangular coverage regions have vertical and slope-2 diagonal boundaries, computed via 2D imos difference arrays in $O(N(N + M) + Q)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc260_g`](../../analysis/AtCoder-abc260_g.md) | G. Scalene Triangle Area | 2339 | Count how many pieces cover each query square in a scalene triangle region. Triangular coverage regions have vertical an... |
