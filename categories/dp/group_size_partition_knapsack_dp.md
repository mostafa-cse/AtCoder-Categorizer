# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Choosing k groups of size s from k*s elements has (k*s)! / ((s!)^k k!) ways. Factoring out (k*s)! aligns with dividing states by j!, allowing knapsack-style DP over group sizes without combinatorial overcounting.
- Common Reductions: Count ways to partition N people into groups of sizes s in [A, B] where group count k is either 0 or in [C, D]. Using exponential generating functions (dividing DP by j!), adding k groups of size s contributes coeff = 1 / ((s!)^k k!) to transition E[j + k*s] += E[j] * coeff in O(N^2 log N) total time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc067_c`](../../analysis/AtCoder-arc067_c.md) | E. Grouping | 2190 | Count ways to partition N people into groups of sizes s in [A, B] where group count k is either 0 or in [C, D]. Using ex... |
