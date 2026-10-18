# Divide and Conquer Optimization

**Taxonomy Path**: `Dynamic Programming (DP)` > `DP Optimizations` > `Divide and Conquer Optimization`

## Description
This topic focuses on divide and conquer optimization techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because $m^*(k)$ satisfies monotonicity, Divide and Conquer Optimization evaluates all $k \in [1, N]$ in $O(N \log N)$ evaluations of $f(k, m)$. Using a Persistent Segment Tree over sorted $A$-values, the sum of the $k - 1$ largest elements in prefix $m - 1$ is queried in $O(\log N)$ time, yielding total time $O(N \log^2 N)$.
- Common Reductions: For each $k = 1 \dots N$, select $k$ pairs $(A_i, B_i)$ to maximize $\sum_{i \in S} A_i - \max_{i \in S} B_i$. Sort pairs by $B_i$ ascending: $B_1 \le B_2 \le \dots \le B_N$. If the maximum $B$ in $S$ is at index $m$, we take $(A_m, B_m)$ and greedily select the $k - 1$ largest $A_i$ among prefix $1 \dots m - 1$. The optimal choice $m^*(k) = \arg\max_m f(k, m)$ is monotonically non-decreasing in $k$: $m^*(1) \le m^*(2) \le \dots \le m^*(N)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc348_g`](../../analysis/AtCoder-abc348_g.md) | G. Max (Sum - Max) | 2559 | For each $k = 1 \dots N$, select $k$ pairs $(A_i, B_i)$ to maximize $\sum_{i \in S} A_i - \max_{i \in S} B_i$. Sort pair... |
