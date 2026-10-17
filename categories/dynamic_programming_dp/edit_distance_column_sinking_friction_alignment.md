# Edit Distance

**Taxonomy Path**: `Dynamic Programming (DP)` > `Classic DP` > `Edit Distance`

## Description
This topic focuses on edit distance techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Total friction cost decomposes additively into independent interactions between adjacent column pairs $(j, j+1)$. The relative sequence of sinking operations for two adjacent columns corresponds to a 2D alignment grid walk from $(0, 0)$ to $(H, H)$, isomorphic to Edit Distance DP.
- Common Reductions: Given an $H \times W$ grid of colored blocks, repeatedly choose a column and lower it by one cell. Whenever two horizontally adjacent blocks share the same color, 1 point of friction cost is incurred. Find the minimum total friction cost to sink all blocks.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-codefestival_2016_qualC_d`](../../analysis/AtCoder-codefestival_2016_qualC_d.md) | D. Friction | 2283 | Given an $H \times W$ grid of colored blocks, repeatedly choose a column and lower it by one cell. Whenever two horizont... |
