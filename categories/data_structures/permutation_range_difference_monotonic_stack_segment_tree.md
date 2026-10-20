# Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum

**Taxonomy Path**: `Data Structures (DS)` > `Monotonic Data Structures` > `Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum`

## Description
This topic focuses on monotonic stack: all nearest smaller values and all subarray maximum/minimum techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For any range [L, R], the quantity f(L, R) = max P_i - min P_i - (R - L) is always >= 0, and f(L, R) = 0 iff the range is a contiguous interval of values. As R advances from 1 to N, monotonic stacks maintain the prefix maximums and minimums, performing range additions on L in [1, R]. Since K <= 3, a lazy segment tree can maintain the minimum value in each node and the counts of elements achieving min_val + d for d in {0, 1, 2, 3}.
- Common Reductions: Given a permutation P of (1, ..., N) and integer K in [0, 3], count pairs (L, R) (1 <= L <= R <= N) such that (max_{L <= i <= R} P_i) - (min_{L <= i <= R} P_i) - (R - L) <= K.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc248_h`](../../analysis/AtCoder-abc248_h.md) | Ex - Beautiful Subsequences | 2968 | Given a permutation P of (1, ..., N) and integer K in [0, 3], count pairs (L, R) (1 <= L <= R <= N) such that (max_{L <=... |
