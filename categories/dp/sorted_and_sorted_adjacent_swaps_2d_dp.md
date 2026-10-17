# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In any valid arrangement, the prefix of length i + j contains the first i white balls and the first j black balls. The number of adjacent swaps to construct a permutation equals the number of inversions. Placing white ball i + 1 next costs the number of remaining unplaced balls that initially appeared before pos(W_{i+1}). This cost decomposes into costW_W[i+1] (unplaced white balls before it) plus costW_B[i+1][j] (unplaced black balls before it), both precomputable in O(N^2).
- Common Reductions: Find the minimum number of adjacent swaps to reorder 2N balls (N white, N black) so that white balls and black balls are each internally sorted 1 to N.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc097_c`](../../analysis/AtCoder-arc097_c.md) | Sorted and Sorted | 2247 | Find the minimum number of adjacent swaps to reorder 2N balls (N white, N black) so that white balls and black balls are... |
