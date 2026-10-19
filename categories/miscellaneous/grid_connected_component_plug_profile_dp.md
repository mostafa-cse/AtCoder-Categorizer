# Broken Profile DP / Plug DP

**Taxonomy Path**: `Miscellaneous` > `General` > `Broken Profile DP / Plug DP`

## Description
This topic focuses on broken profile dp / plug dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because M <= 7, this is a canonical Broken Profile / Plug DP problem. When processing cell by cell (i, j), we maintain the connectivity profile of the frontier of length M+1 (the latest cell of each column). The partition of frontier black cells into connected components has at most B_7 = 877 states, which can be canonically renumbered. As cells are colored black or left white, components are merged or closed. A closed component cannot be abandoned if there are remaining original black cells.
- Common Reductions: Given an N x M grid (M <= 7) with black and white cells containing at least one black cell, find the minimum number of white cells to paint black so that all black cells form a single connected component.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc296_h`](../../analysis/AtCoder-abc296_h.md) | Ex - Unite | 2822 | Given an N x M grid (M <= 7) with black and white cells containing at least one black cell, find the minimum number of w... |
