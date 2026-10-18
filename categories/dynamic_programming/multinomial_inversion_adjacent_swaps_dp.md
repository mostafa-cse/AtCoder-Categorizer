# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Every distinct string T reachable from S corresponds uniquely to a permutation preserving identical characters' relative order. The minimum number of adjacent swaps to reach T is precisely the inversion count of this canonical permutation. State dp[cK][cE][cY][inv] tracks the number of prefixes with exact inversion count, transitioning by placing the next character and counting unplaced preceding characters.
- Common Reductions: Count distinct strings reachable from a ternary string of characters 'K', 'E', 'Y' (|S| <= 30) using at most K adjacent swaps. Since each distinct string corresponds uniquely to the permutation preserving identical characters' relative order, state dp[cK][cE][cY][inv] tracks minimum inversions to place prefixes, running in O(|S|^5) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc227_e`](../../analysis/AtCoder-abc227_e.md) | E. Swap | 2377 | Count distinct strings reachable from a ternary string of characters 'K', 'E', 'Y' (|S| <= 30) using at most K adjacent ... |
