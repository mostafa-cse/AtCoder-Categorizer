# Catalan Numbers

**Taxonomy Path**: `Combinatorics` > `Catalan` > `Catalan Numbers`

## Description
This topic focuses on catalan numbers techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Polish sequences correspond to lattice paths strictly above a boundary (Ballot theorem / Catalan lattice paths). If we deviate from A at index i with a choice x < A[i], the remaining suffix of length L = N - i must complete the path to total excess -1 without dropping below 0 before the end. The number of such completions from current excess h is given by F(L, h) = C(2L - 1 - h, L - 1) - C(2L - 1 - h, L). Summing F(L, h) over the valid choices of x < A[i] telescopes via the hockey-stick identity on Pascal's triangle into a closed form evaluable in O(1) time.
- Common Reductions: A sequence of non-negative integers A is a Polish sequence if it corresponds to Polish prefix notation of a tree: every proper prefix sum sum_{j=1}^k (a_j - 1) >= 0 and the full sum is -1. Count Polish sequences of length N that are lexicographically <= A, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc186_d`](../../analysis/AtCoder-arc186_d.md) | D - Polish Mania | 2776 | A sequence of non-negative integers A is a Polish sequence if it corresponds to Polish prefix notation of a tree: every ... |
