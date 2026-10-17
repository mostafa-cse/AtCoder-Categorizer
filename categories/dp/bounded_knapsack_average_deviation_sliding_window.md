# Knapsack and Subset Sum Optimizations

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Subset Sum Optimizations`

## Description
This topic focuses on knapsack and subset sum optimizations techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The average of a multiset is $x$ if and only if the sum of deviations $\sum_{i=1}^N c_i (i - x) = 0$. For elements $i < x$, deviations are negative with weights $d = x - i \in [1, x-1]$; for elements $i > x$, deviations are positive with weights $d = i - x \in [1, N-x]$. The positive and negative deviation sums must be equal to some sum $S \ge 0$.
Let $DP[L][S]$ be the number of ways to form sum $S$ using weights $\{1, \dots, L\}$ with multiplicity $\le K$. For each $x$, the answer is $K + (K+1) \sum_{S \ge 1} DP[x-1][S] \cdot DP[N-x][S] \pmod M$. Precomputing $DP[L][S]$ takes $O(K N^3)$ via prefix sliding window.
- Common Reductions: Given positive integers $N, K$ and prime $M$, for every integer $x \in [1, N]$, find the number of non-empty multisets of elements from $\{1, \dots, N\}$ with multiplicity at most $K$ such that the average of the elements is $x$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc104_d`](../../analysis/AtCoder-arc104_d.md) | D. Multiset Mean | 2251 | Given positive integers $N, K$ and prime $M$, for every integer $x \in [1, N]$, find the number of non-empty multisets o... |
