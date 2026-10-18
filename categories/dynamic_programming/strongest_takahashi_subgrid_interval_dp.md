# Interval DP / Range DP / Matrix Chain Multiplication (MCM)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Classic DP` > `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`

## Description
This topic focuses on interval dp / range dp / matrix chain multiplication (mcm) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any subgrid without '#' costs 0. For any subgrid with '#', we can either cover it entirely with one square of size $\max(\Delta r, \Delta c)$, or divide it into two independent subproblems by cutting across a row or column.
- Common Reductions: Given an $N \times N$ grid ($N \le 50$) with '#' squares, find the minimum cost to destroy all '#' using $D \times D$ subsquares at cost $D$. A 4D subgrid interval DP $dp[r_1][r_2][c_1][c_2]$ computes the optimal cost by taking the base square cost $\max(r_2 - r_1 + 1, c_2 - c_1 + 1)$ and taking the minimum over all horizontal cuts $r_1 \le k < r_2$ and vertical cuts $c_1 \le k < c_2$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc233_g`](../../analysis/AtCoder-abc233_g.md) | G. Strongest Takahashi | 2438 | Given an $N \times N$ grid ($N \le 50$) with '#' squares, find the minimum cost to destroy all '#' using $D \times D$ su... |
