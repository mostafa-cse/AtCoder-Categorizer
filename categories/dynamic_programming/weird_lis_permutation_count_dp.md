# Longest Increasing Subsequence (LIS)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Classic DP` > `Longest Increasing Subsequence (LIS)`

## Description
This topic focuses on longest increasing subsequence (lis) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By Schensted's theorem and the Robinson-Schensted correspondence, the LIS corresponds to the length of the first row of the insertion tableau. The problem imposes invariant bounds on the prefix maxima and LIS values. Reformulating the condition into forbidden subsequence patterns enables dynamic programming over active prefix bounds and insertion frontiers in O(N^2) time.
- Common Reductions: Count the number of permutations of (1..N) that satisfy specified conditions on the length of their Longest Increasing Subsequence (LIS) under cyclic shifts or pattern constraints.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc055_c`](../../analysis/AtCoder-agc055_c.md) | C - Weird LIS | 2803 | Count the number of permutations of (1..N) that satisfy specified conditions on the length of their Longest Increasing S... |
