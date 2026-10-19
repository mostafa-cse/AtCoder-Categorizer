# Interval DP / Range DP / Matrix Chain Multiplication (MCM)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Classic DP` > `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`

## Description
This topic focuses on interval dp / range dp / matrix chain multiplication (mcm) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: This is equivalent to the Cocke-Younger-Kasami (CYK) dynamic programming algorithm for parsing context-free grammars. The minimum cost to derive substring T[l..r] from a single non-terminal c, dp[c][l][r], can be computed by splitting T[l..r] into segments corresponding to characters of the replacement string A. Transitions alternate between interval-splitting DP across substring lengths and Dijkstra's algorithm on unit-cost single-character derivations.
- Common Reductions: Given a starting string S, a target string T, and K replacement operations c_i -> A_i, find the minimum number of replacements to transform S into T, or report -1 if impossible.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc261_g`](../../analysis/AtCoder-abc261_g.md) | G - Replace | 2803 | Given a starting string S, a target string T, and K replacement operations c_i -> A_i, find the minimum number of replac... |
