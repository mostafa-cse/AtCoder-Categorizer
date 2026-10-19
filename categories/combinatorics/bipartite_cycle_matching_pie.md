# Principle of Inclusion and Exclusion (PIE)

**Taxonomy Path**: `Combinatorics` > `Inclusion Exclusion` > `Principle of Inclusion and Exclusion (PIE)`

## Description
This topic focuses on principle of inclusion and exclusion (pie) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By Principle of Inclusion-Exclusion, count permutations r violating at least k constraints (r_i = p_i or r_i = q_i). Form a 2-regular bipartite graph between position indices i and value vertices p_i, q_i. Choosing k violations corresponds to choosing a matching of size k in this graph. The graph decomposes into disjoint simple cycles and paths. For a cycle of length 2L, the number of matchings of size k is (2L / (2L - k)) * binom(2L - k, k). Convolving the matching polynomials across all components yields the coefficient sequence c_k. The final answer is sum_{k=0}^N (-1)^k c_k (N - k)!.
- Common Reductions: Given two permutations p and q of length N, count the number of permutations r such that r_i != p_i and r_i != q_i for all 1 <= i <= N, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc214_g`](../../analysis/AtCoder-abc214_g.md) | G. Three Permutations | 2893 | Given two permutations p and q of length N, count the number of permutations r such that r_i != p_i and r_i != q_i for a... |
