# Basic Greedy Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Greedy Algorithms`

## Description
This topic focuses on basic greedy algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For any two intervals with L_1 < L_2 and R_1 < R_2, FIFO pairing (L_1, R_1) and (L_2, R_2) yields min(R_1 - L_1, R_2 - L_2) >= min(R_1 - L_2, R_2 - L_1). Thus FIFO matching dominates all other matchings. Intervals starting at -inf or ending at +inf have infinite length and are ignored.
- Common Reductions: Given point coverage requirements y_i at coordinates x_i, positive differences y_i - y_{i-1} start intervals at x_{i-1} + 1, and negative differences y_{i-1} - y_i end intervals at x_i - 1. Maximizing min(R_j - L_j) is solved by FIFO queue matching between starts and ends.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc166_d`](../../analysis/AtCoder-arc166_d.md) | D. Interval Counts | 2192 | Given point coverage requirements y_i at coordinates x_i, positive differences y_i - y_{i-1} start intervals at x_{i-1} ... |
