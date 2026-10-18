# Substring DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `Substring DP`

## Description
This topic focuses on substring dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: When concatenating strings, substrings can either be entirely contained within one of the original strings, or cross the concatenation boundary between adjacent strings. By filtering redundant strings and grouping concatenation lengths, we define a dynamic programming state over suffix matches and boundary overlaps.
- Common Reductions: Given N strings S_i, we want to concatenate a subset of them into a single string. Count the number of distinct substrings of the concatenated string across all valid orderings, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc416_g`](../../analysis/AtCoder-abc416_g.md) | G. Concat (1st) | 2542 | Given N strings S_i, we want to concatenate a subset of them into a single string. Count the number of distinct substrin... |
