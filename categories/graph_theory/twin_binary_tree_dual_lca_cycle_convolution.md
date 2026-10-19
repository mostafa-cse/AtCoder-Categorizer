# Binary Lifting and LCA

**Taxonomy Path**: `Graph Theory` > `Lowest Common Ancestor (LCA)` > `Binary Lifting and LCA`

## Description
This topic focuses on binary lifting and lca techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Iterate over each internal node a in T_1. The node a is the LCA in T_1 for all pairs (u, v) where u is in the left subtree L(a) and v is in the right subtree R(a). For a fixed a, LCA_1 is constant. For each u in L(a), trace up T_2 from P(u) to the root, adding path weights to ancestor counters. Then for each v in R(a), trace up T_2 from P(v), accumulating contributions where the meeting node in T_2 is the exact LCA_2. Clearing the table keeps the total complexity proportional to subtree sizes.
- Common Reductions: Two perfect binary trees of depth H share the same 2^{H-1} leaves via a leaf permutation P. Compute the sum of weights over all pairs of leaves (u, v), where weight depends on the depths of LCA_1(u, v) and LCA_2(P(u), P(v)).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc047_d`](../../analysis/AtCoder-agc047_d.md) | D. Twin Binary Trees | 2910 | Two perfect binary trees of depth H share the same 2^{H-1} leaves via a leaf permutation P. Compute the sum of weights o... |
