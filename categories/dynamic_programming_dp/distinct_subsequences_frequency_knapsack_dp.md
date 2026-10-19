# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Process frequencies in descending order i = N, N-1, ..., 1. When transitioning from frequency i + 1 to i, decide how many values l will have frequency exactly i. Since each such value contributes i occurrences, the total frequency is bounded by N, meaning at most N / i values can have frequency >= i. The DP state is dp[j][k], where j values have frequency >= i and k total positions are filled. Transitions use combinations for choosing which values and positions receive frequency i, leading to a harmonic DP running in O(N^2 log N).
- Common Reductions: Given an array A of length N with some elements already fixed and others 0, count the number of completions such that for every value x, its frequency in the completion does not exceed B_x, and the number of elements with frequency >= f satisfies given constraints.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc162_e`](../../analysis/AtCoder-arc162_e.md) | E - Small Multiple Permutation | 2780 | Given an array A of length N with some elements already fixed and others 0, count the number of completions such that fo... |
