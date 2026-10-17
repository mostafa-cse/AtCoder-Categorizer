# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In any sorted array, all negative elements (requiring $2c_i + 1$ operations) must precede all positive elements (requiring $2d_i$ operations). For a fixed suffix, the required powers satisfy $d_j = P_j - \min_{k=i}^j P_k$ where $P_k$ is the prefix sum of relative scale adjustments.
- Common Reductions: Given array $A$ of length $N$, find the minimum number of operations (multiplying an element by 4 or dividing by 4) to make $A$ non-decreasing, allowing negative values via optimal sign assignment.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-caddi2018_c`](../../analysis/AtCoder-caddi2018_c.md) | E. Negative Doubling | 2327 | Given array $A$ of length $N$, find the minimum number of operations (multiplying an element by 4 or dividing by 4) to m... |
