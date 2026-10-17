# Interval DP / Range DP / Matrix Chain Multiplication (MCM)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Classic DP` > `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`

## Description
This topic focuses on interval dp / range dp / matrix chain multiplication (mcm) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Let dp[l][r] count valid trees rooted at a virtual node 0 covering the subsequence A[l..r-1]. The first child of 0 is A[l]. Either A[l] is the sole child of 0 (all remaining elements are in A[l]'s subtree, counted by dp[l+1][r]), or 0 has subsequent children. If the next child of 0 is A[k] (l+1 <= k < r), the condition that siblings are visited in increasing order demands A[l] < A[k]. Subtree of A[l] covers [l+1, k) and the remaining forest covers [k, r).
- Common Reductions: Given the DFS preorder sequence of a rooted tree where children of any vertex are visited in strictly increasing numerical order, count the number of valid rooted tree topologies modulo 998244353. Solved via interval DP tracking valid forests under root order constraints.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| `[problem:AtCoder-abc252_g]` | Pre-Order | 2153 | Given the DFS preorder sequence of a rooted tree where children of any vertex are visited in strictly increasing numeric... |
