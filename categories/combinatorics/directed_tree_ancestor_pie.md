# Principle of Inclusion and Exclusion (PIE)

**Taxonomy Path**: `Combinatorics` > `Inclusion Exclusion` > `Principle of Inclusion and Exclusion (PIE)`

## Description
This topic focuses on principle of inclusion and exclusion (pie) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The bad condition is that a_i is a proper ancestor of i. By the Principle of Inclusion-Exclusion, we count ways to choose k pairs (u, a_u) where a_u is a proper ancestor of u. Reversing the perspective, ancestor v chooses a proper descendant u. In post-order traversal, if j descendant choices were already made in the subtree of v, exactly sz(v) - 1 - j proper descendants remain available for v to choose. This independence allows subtree knapsack DP in O(N^2).
- Common Reductions: Given a directed tree rooted at 1, find the number of permutations a of (1 ... N) such that for every i, i is unreachable from a_i by traversing 1 or more edges, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc121_e`](../../analysis/AtCoder-arc121_e.md) | E - Directed Tree | 2645 | Given a directed tree rooted at 1, find the number of permutations a of (1 ... N) such that for every i, i is unreachabl... |
