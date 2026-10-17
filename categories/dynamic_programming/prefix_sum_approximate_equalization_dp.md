# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The total sum $S = \sum A_i$ is invariant under adjacent transfer. The target sequence $B$ consists of exactly $r = S \bmod N$ elements equal to $q + 1$ and $N - r$ elements equal to $q = \lfloor S / N \rfloor$. The minimum operations equals $\sum_{i=1}^{N-1} |\text{pref}_A[i] - \text{pref}_B[i]|$.
- Common Reductions: Given array $A$ of length $N$, you can repeatedly choose an index $i$ and replace $(A_i, A_{i+1})$ with $(A_i - 1, A_{i+1} + 1)$. Minimize the sum of squared differences or prefix sum deviations to equalize the elements.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc307_g`](../../analysis/AtCoder-abc307_g.md) | G. Approximate Equalization | 2330 | Given array $A$ of length $N$, you can repeatedly choose an index $i$ and replace $(A_i, A_{i+1})$ with $(A_i - 1, A_{i+... |
