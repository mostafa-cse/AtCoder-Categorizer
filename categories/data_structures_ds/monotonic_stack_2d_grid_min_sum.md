# Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum

**Taxonomy Path**: `Data Structures (DS)` > `Monotonic Data Structures` > `Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum`

## Description
This topic focuses on monotonic stack: all nearest smaller values and all subarray maximum/minimum techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Iterate over all $O(N^2)$ row boundary pairs $[u, d]$. For a fixed pair $[u, d]$, collapse columns into two 1D arrays: column sum $S_j = \sum_{i=u}^d A_{i, j}$ and column minimum $B_j = \min_{i=u}^d A_{i, j}$. Any subsegment of columns $[l, r]$ has subgrid sum $\sum_{j=l}^r S_j$ and minimum $\min_{j=l}^r B_j$. Because all entries $A_{i,j} \ge 1 > 0$, column sums are strictly positive; thus, for a column $k$ acting as the minimum, extending the column range as far left and right as possible while $B_j \ge B_k$ strictly maximizes the sum. Using a monotonic stack, we find the maximal span $[L_k, R_k]$ for each column $k$ in $O(M)$ time.
- Common Reductions: Given an $N \times M$ grid of non-negative integers ($N, M \le 300, A_{i,j} \le 300$), select a rectangular subgrid $R$ to maximize $(\sum_{(i,j) \in R} A_{i,j}) \times \min_{(i,j) \in R} A_{i,j}$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc311_g`](../../analysis/AtCoder-abc311_g.md) | G. One More Grid Task | 2265 | Given an $N \times M$ grid of non-negative integers ($N, M \le 300, A_{i,j} \le 300$), select a rectangular subgrid $R$ ... |
