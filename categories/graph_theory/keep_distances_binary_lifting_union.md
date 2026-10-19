# Binary Lifting and LCA

**Taxonomy Path**: `Graph Theory` > `Lowest Common Ancestor (LCA)` > `Binary Lifting and LCA`

## Description
This topic focuses on binary lifting and lca techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Let m be the maximum size of a good set in [L, R]. Greedy selection from left to right yields indices a_1 < a_2 < ... < a_m, and greedy selection from right to left yields b_1 < b_2 < ... < b_m. It holds that a_1 <= b_1 < a_2 <= b_2 < ... < a_m <= b_m. A point p belongs to some good set if and only if p in [a_i, b_i] for some i. The size of the union is sum_{i=1}^m (b_i - a_i + 1) = m + sum b_i - sum a_i. Both the sequence a_i and b_i and their index sums can be computed using binary lifting (doubling) in O(log N) per query.
- Common Reductions: Given N points on a line X_1 < ... < X_N and an integer K, process Q queries. Each query gives [L, R]. A good set is a maximum-size subset of points in [L, R] with pairwise distance >= K. Find the size of the union of all good sets.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-acl1_d`](../../analysis/AtCoder-acl1_d.md) | D - Keep Distances | 2764 | Given N points on a line X_1 < ... < X_N and an integer K, process Q queries. Each query gives [L, R]. A good set is a m... |
