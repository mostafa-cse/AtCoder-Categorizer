# Interval DP / Range DP / Matrix Chain Multiplication (MCM)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Classic DP` > `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`

## Description
This topic focuses on interval dp / range dp / matrix chain multiplication (mcm) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Simulating forward is intractable because card values grow dynamically depending on previous choices. Instead, reverse the process: consider the LAST card k eaten among internal cards in interval (i, j). If card i has final multiplier c_i and card j has final multiplier c_j, then card k will contribute (c_i + c_j) * A_k to the final answer. Card k then splits the interval into subproblems (i, k) and (k, j), each inheriting the respective multiplier c_i + c_j for card k. This induces an interval DP with state (i, j, c_i, c_j).
- Common Reductions: Given an array A of N cards, repeatedly choose three adjacent cards, eat the middle one, add its value to its two neighbors, and discard it, until 2 cards remain. Minimize the sum of the remaining two cards.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc035_d`](../../analysis/AtCoder-agc035_d.md) | D. Add and Remove | 2902 | Given an array A of N cards, repeatedly choose three adjacent cards, eat the middle one, add its value to its two neighb... |
