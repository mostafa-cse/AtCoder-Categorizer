# Knapsack and Subset Sum Optimizations

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Subset Sum Optimizations`

## Description
This topic focuses on knapsack and subset sum optimizations techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In dimension $i$ with coordinate difference $d = |p_i - q_i|$, choosing $r_i$ adds $(\Delta_p, \Delta_q) = (|r_i - p_i|, |r_i - q_i|)$. Over all possible integers $r_i$, the pair of step distances sweeps a trapezoidal segment where $\Delta_p - \Delta_q$ or $\Delta_p + \Delta_q$ is constant, allowing constant-time range updates via 2D diagonal prefix sums.
- Common Reductions: Given two points $P, Q \in \mathbb{R}^N$, count the number of integer points $R \in \mathbb{Z}^N$ such that $d(P, R) \le D$ and $d(Q, R) \le D$ under the Manhattan distance metric, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc265_f`](../../analysis/AtCoder-abc265_f.md) | F. Manhattan Cafe | 2290 | Given two points $P, Q \in \mathbb{R}^N$, count the number of integer points $R \in \mathbb{Z}^N$ such that $d(P, R) \le... |
