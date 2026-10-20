# Interval DP / Range DP / Matrix Chain Multiplication (MCM)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Classic DP` > `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`

## Description
This topic focuses on interval dp / range dp / matrix chain multiplication (mcm) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any grid of size H x W can be partitioned with complexity at most ceil(log_2 H) + ceil(log_2 W) <= 16. Rather than computing complexity for every 4D subgrid [u, d, l, r] (which would require O(H^2 W^2) states), we invert the DP: fix complexity k in [0, 16], and let dp[u][d][l] denote the maximum right column r such that subgrid [u, d] x [l, r-1] has complexity <= k.
- Common Reductions: Given an H x W grid (H, W <= 185) with '#' and '.', find the minimum complexity to partition the grid into monochromatic rectangles, where complexity of monochromatic is 0, and a split into A, B has complexity 1 + max(c(A), c(B)).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc033_d`](../../analysis/AtCoder-agc033_d.md) | D - Complexity | 2962 | Given an H x W grid (H, W <= 185) with '#' and '.', find the minimum complexity to partition the grid into monochromatic... |
