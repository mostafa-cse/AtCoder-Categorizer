# Longest Increasing Subsequence (LIS)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Classic DP` > `Longest Increasing Subsequence (LIS)`

## Description
This topic focuses on longest increasing subsequence (lis) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If the path can turn at $k$ fountains without forcing a U-turn, it saves $k \times (20 - 5\pi)$. If $k = \min(|x_2 - x_1|, |y_2 - y_1|) + 1$, the path is forced to pass through every row and column, meaning one fountain must be traversed via a semicircle (adding $10\pi - 20$) rather than a quarter-circle.
- Common Reductions: Find the shortest distance from $(x_1, y_1)$ to $(x_2, y_2)$ on a grid of roads where fountains of radius 10 occupy integer intersections. Walking along the circular circumference of a fountain saves $20 - 5\pi$ distance compared to walking around its bounding square, provided the path turns by 90 degrees around the quarter-circle. Within the bounding box $[x_1, x_2] \times [y_1, y_2]$, any monotone path that turns at fountains can utilize at most one fountain per $x$ and $y$ coordinate. Finding the maximum number of usable fountains is equivalent to finding the Longest Increasing Subsequence (LIS) of fountain coordinates.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc019_c`](../../analysis/AtCoder-agc019_c.md) | C. Fountain Walk | 2495 | Find the shortest distance from $(x_1, y_1)$ to $(x_2, y_2)$ on a grid of roads where fountains of radius 10 occupy inte... |
