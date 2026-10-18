# Divide and Conquer

**Taxonomy Path**: `Basics` > `Divide and Conquer` > `Divide and Conquer`

## Description
This topic focuses on divide and conquer techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Shortest paths never leave the bounding column range [c_1, c_2]. Divide and conquer on columns [L, R] with midpoint M: any path from X in [L, M] to Y in [M+1, R] crosses from M to M+1 exactly once, using either top edge (1, M)-(1, M+1) or bottom edge (2, M)-(2, M+1). The shortest distance is min(d_top(X) + d_top(Y), d_bot(X) + d_bot(Y)). The condition d_top(X) - d_bot(X) <= d_bot(Y) - d_top(Y) separates which boundary edge is optimal, solved by binary search on sorted right differences.
- Common Reductions: In a 2 x N grid with positive vertex weights, find the sum of shortest path weights over all pairs of squares (X, Y) modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc158_e`](../../analysis/AtCoder-arc158_e.md) | E - All-Pair Shortest Paths | 2641 | In a 2 x N grid with positive vertex weights, find the sum of shortest path weights over all pairs of squares (X, Y) mod... |
