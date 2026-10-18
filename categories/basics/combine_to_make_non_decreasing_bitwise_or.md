# Bitwise Operations and Bitmasks

**Taxonomy Path**: `Basics` > `Bitwise Thinking` > `Bitwise Operations and Bitmasks`

## Description
This topic focuses on bitwise operations and bitmasks techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For each right endpoint $r$, as the left endpoint $l$ decreases, the range OR $f(l, r) = A_l \mid \dots \mid A_r$ takes at most 30 distinct values. There are $O(N \log(\max A))$ such contiguous intervals $[l_1, l_2)$ for each $r$. Sorting all intervals primarily by their OR value ascending and secondarily by $r$ allows a 1D DP where $dp[r+1] = \max(dp[r+1], \max_{l_1 \le l < l_2} dp[l] + 1)$, optimized with a Segment Tree in $O(N \log(\max A) \log N)$ time.
- Common Reductions: Maximize the number of segments after partitioning $A$ such that the bitwise OR of each segment forms a non-decreasing sequence.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc207_c`](../../analysis/AtCoder-arc207_c.md) | C - Combine to Make Non-decreasing | 2488 | Maximize the number of segments after partitioning $A$ such that the bitwise OR of each segment forms a non-decreasing s... |
