# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Only elements where the added cumulative sum is non-zero actually change. To avoid double-counting distinct subsequences producing the same modified array, canonicalize transitions: maintain dp1[i][j] (number of valid modified prefixes ending at i with current cumulative sum j) and dp2[i][j] (count where the last selected element was j, meaning sum before was 0). When transitioning from sum 0, subtract dp2[i][a_{i+1}] to eliminate duplicate prefix sums.
- Common Reductions: Count the number of distinct sequences obtainable by replacing a chosen non-empty subsequence with its cumulative prefix sums.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc180_c`](../../analysis/AtCoder-arc180_c.md) | Subsequence and Prefix Sum | 2221 | Count the number of distinct sequences obtainable by replacing a chosen non-empty subsequence with its cumulative prefix... |
