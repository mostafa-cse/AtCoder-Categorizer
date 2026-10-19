# Partitions of a Set / Bell Number

**Taxonomy Path**: `Combinatorics` > `Partitions` > `Partitions of a Set / Bell Number`

## Description
This topic focuses on partitions of a set / bell number techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For N <= 6, the relative order of elements X_1, ..., X_N is governed by one of the F(6) = 4683 ordered set partitions (weak orderings). For a fixed weak ordering, the LIS is deterministic. The number of integer assignments Y_1 < Y_2 < ... < Y_k satisfying Y_j <= min_{i in part j} A_i is computed using interval DP over the O(N) coordinate intervals formed by breakpoints {0} union {A_i}.
- Common Reductions: Given N <= 6 and upper bounds A_1, ..., A_N, random variables X_i are chosen uniformly from [1, A_i]. Compute the expected length of the Longest Increasing Subsequence (LIS) of X modulo 1000000007.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc104_e`](../../analysis/AtCoder-arc104_e.md) | E - Random LIS | 2824 | Given N <= 6 and upper bounds A_1, ..., A_N, random variables X_i are chosen uniformly from [1, A_i]. Compute the expect... |
