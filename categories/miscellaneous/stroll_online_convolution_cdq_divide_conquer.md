# CDQ Divide and Conquer

**Taxonomy Path**: `Miscellaneous` > `Techniques` > `CDQ Divide and Conquer`

## Description
This topic focuses on cdq divide and conquer techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The DP state dp[v][t] = sum_{(u, v)} sum_{k=1}^t dp[u][t - k] * P(e, k) is a system of mutually recursive online convolutions. Using CDQ Divide and Conquer with NTT, the self-referential transitions can be computed offline in O(M * T log^2 T) time by splitting the time range [L, R] at mid, solving [L, mid], convolving [L, mid] with P(e) to push contributions into [mid + 1, R], and recursing on [mid + 1, R].
- Common Reductions: In a graph with time-dependent transition probabilities P(e, t), find the probability of a random stroll starting at vertex 1 returning to vertex 1 at time T, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc213_h`](../../analysis/AtCoder-abc213_h.md) | H - Stroll | 2806 | In a graph with time-dependent transition probabilities P(e, t), find the probability of a random stroll starting at ver... |
