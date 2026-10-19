# Permutations, Combinations and Basic Counting Problems

**Taxonomy Path**: `Basics` > `Basic Counting` > `Permutations, Combinations and Basic Counting Problems`

## Description
This topic focuses on permutations, combinations and basic counting problems techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The lexicographical rank of permutation P is 1 + sum_{i=1}^N c_i (N - i)!, where c_i is the count of j > i with P_j < P_i. By linearity of expectation, sum c_i over completions by partitioning pairs (i, j) into four types: fixed-fixed, fixed-free, free-fixed, and free-free. Using a Fenwick tree and prefix sums of unused numbers, each type can be counted in O(N log N) time.
- Common Reductions: Given a partial permutation of length N with some known values and some missing values, find the sum of lexicographical ranks over all valid completions modulo 10^9+7.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-codefestival_2016_qualC_e`](../../analysis/AtCoder-codefestival_2016_qualC_e.md) | E. Encyclopedia of Permutations | 2885 | Given a partial permutation of length N with some known values and some missing values, find the sum of lexicographical ... |
