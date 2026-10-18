# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Reverse the string $S$: the forbidden pattern becomes $C' \dots c' \dots C \dots C$. A reversed string is valid iff no duplicate uppercase letter appears after the first lowercase letter following an uppercase letter. Use DP on the prefix of reversed $S$ to track uppercase presence, and combinatorics on remaining question marks to count valid assignments of distinct uppercase letters.
- Common Reductions: Count replacements of '?' with letters such that no 'DDoS'-like subsequence ($C \dots C \dots c' \dots C'$ with uppercase $C, C'$ and lowercase $c'$) is formed.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc301_f`](../../analysis/AtCoder-abc301_f.md) | F. Anti-DDoS | 2548 | Count replacements of '?' with letters such that no 'DDoS'-like subsequence ($C \dots C \dots c' \dots C'$ with uppercas... |
