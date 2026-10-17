# 2D Prefix Sum

**Taxonomy Path**: `Basics` > `2D Prefix Sum` > `2D Prefix Sum`

## Description
This topic focuses on 2d prefix sum techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The problem states that between any two blue cells there is at most one simple path, meaning the blue cells form an induced forest. In any forest graph, the number of connected components equals V - E, where V is the number of vertices and E is the number of edges. Any induced subgraph of a forest is also a forest. Thus, in any query rectangle [x1, x2] x [y1, y2], Components = V - (E_horizontal + E_vertical). All three quantities are rectangle sum queries on static binary grids, computable in O(1) using 2D prefix sums.
- Common Reductions: Answer Q queries counting connected components of blue cells in arbitrary subgrids of an N x M grid where blue cells form an induced forest.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc015_c`](../../analysis/AtCoder-agc015_c.md) | Nuske vs Phantom Thnook | 2241 | Answer Q queries counting connected components of blue cells in arbitrary subgrids of an N x M grid where blue cells for... |
