# Grundy Number and Basic Game Theory

**Taxonomy Path**: `Game Theory` > `Grundy Number / Nim` > `Grundy Number and Basic Game Theory`

## Description
This topic focuses on grundy number and basic game theory techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By the Sprague-Grundy theorem, the game is equivalent to standard Nim with Grundy values g(A_i). Let S = {0, X_1, ..., X_M} be the set of critical pile sizes. If n not in S, no moves from n are forbidden, so g(n) = h(n-1) + 1, where h(n) = max_{0..n} g(i). Between critical points, g(n) = n - n_bar + h(n_bar), where n_bar is the predecessor in S. At each critical point n in S, the forbidden moves eliminate a small set of transitions. By tracking duplicate Grundy values in a frequency map, we can compute mex in O(deg(n)) per critical point. The total time to process S is O(M log M), and queries take O(log M).
- Common Reductions: We play Nim with N piles of sizes A_i <= 10^{18}. There are M forbidden moves: removing Y_i stones from a pile of size X_i is forbidden. Find which player wins under optimal play.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc255_g`](../../analysis/AtCoder-abc255_g.md) | G - Constrained Nim | 2734 | We play Nim with N piles of sizes A_i <= 10^{18}. There are M forbidden moves: removing Y_i stones from a pile of size X... |
