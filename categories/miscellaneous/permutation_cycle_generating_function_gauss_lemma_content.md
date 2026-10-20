# Permutations and Permutation Cycles

**Taxonomy Path**: `Miscellaneous` > `Permutations` > `Permutations and Permutation Cycles`

## Description
This topic focuses on permutations and permutation cycles techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Sorting a so that a_1 <= ... <= a_N, inserting element i+1 into an existing cycle has i choices and does not change the cycle minimum, while forming a new cycle has 1 choice and multiplies beauty by a_{i+1}. The generating function for the cycle partition polynomial is P_N(t) = \prod_{i=0}^{N-1} (a_{i+1} t + i). By Gauss's Lemma on polynomial content, the GCD of all coefficients of a product of integer polynomials equals the product of their contents: c(P_N(t)) = \prod_{i=0}^{N-1} \gcd(a_{i+1}, i).
- Common Reductions: Find the greatest common divisor of b_1, ..., b_N modulo 998244353, where b_k is the sum of cycle products of the minimum chicken size over all permutations with exactly k disjoint cycles.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-dwacon5th_prelims_e`](../../analysis/AtCoder-dwacon5th_prelims_e.md) | E - Cyclic GCDs | 2978 | Find the greatest common divisor of b_1, ..., b_N modulo 998244353, where b_k is the sum of cycle products of the minimu... |
