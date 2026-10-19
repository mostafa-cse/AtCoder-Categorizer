# Principle of Inclusion and Exclusion (PIE)

**Taxonomy Path**: `Combinatorics` > `Inclusion Exclusion` > `Principle of Inclusion and Exclusion (PIE)`

## Description
This topic focuses on principle of inclusion and exclusion (pie) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: First, filter elements to those satisfying (A_i & S) == S and (A_i | T) == T. The remaining varying bits are B = {b : S_b == 0 and T_b == 1}, with |B| <= 18. For each bit b in B, a violation occurs if all chosen elements have bit b = 0 or all chosen elements have bit b = 1. By the Principle of Inclusion-Exclusion, for any subset of bits U in B, all chosen elements violating all bits in U must have the exact same bit pattern on U (i.e. belong to the same equivalence class of x & U). The number of valid subsets is sum_{U in 2^B} (-1)^{|U|} sum_{groups g} sum_{r=1}^{min(K, |g|)} binom(|g|, r). For M <= N <= 50 and 2^18 masks, this runs in O(2^L * M log M) time.
- Common Reductions: Given N pairwise distinct integers A_1, ..., A_N, find the number of subsets of size 1 <= r <= K such that their bitwise AND is S and bitwise OR is T.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-tokiomarine2020_e`](../../analysis/AtCoder-tokiomarine2020_e.md) | E - O(rand) | 2757 | Given N pairwise distinct integers A_1, ..., A_N, find the number of subsets of size 1 <= r <= K such that their bitwise... |
