# Permutations and Permutation Cycles

**Taxonomy Path**: `Miscellaneous` > `Permutations` > `Permutations and Permutation Cycles`

## Description
This topic focuses on permutations and permutation cycles techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each permutation P and Q decomposes into disjoint directed cycles. A ball can reach box X iff it starts on the cycle containing X; otherwise return -1. Moving the furthest ball to X along a cycle naturally sweeps all intermediate balls to X. Thus, red balls require a sequence of operations A along cycle C_P, and blue balls require sequence B along cycle C_Q. Any valid sequence of operations contains both A and B as subsequences. Finding the shortest common supersequence of two sequences of distinct elements reduces to |A| + |B| - LCS(A, B), which is computed via Longest Increasing Subsequence (LIS) in O(N log N).
- Common Reductions: Move all red and blue balls from N boxes to target box X using permutations P and Q with the minimum number of box operations.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc189_c`](../../analysis/AtCoder-arc189_c.md) | Balls and Boxes | 2239 | Move all red and blue balls from N boxes to target box X using permutations P and Q with the minimum number of box opera... |
