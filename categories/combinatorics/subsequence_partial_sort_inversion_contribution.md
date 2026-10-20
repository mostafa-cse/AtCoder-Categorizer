# Contribution Technique

**Taxonomy Path**: `Combinatorics` > `Techniques` > `Contribution Technique`

## Description
This topic focuses on contribution technique techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Decompose inversions by contribution technique: Type 1 inversions between two chosen or two unchosen elements contribute 2^{N-2} I(P). Type 2 inversions between an unchosen element P_i and the sorted chosen elements equal B + D - 2 min(b, d), where B is smaller elements and D is larger elements in P. Summing over all subsets reduces to evaluating sum binom(B, b) binom(D, d) min(b, d) = B sum_{k=0}^{D-1} binom(B+D-1, k) + D sum_{k=0}^{B-2} binom(B+D-1, k), evaluated in O(N sqrt(N)) via Mo's algorithm or linear shift.
- Common Reductions: Given a permutation P of length N, for each of the 2^N subsequences, sort the elements in the subsequence in place while leaving other elements in their original positions. Find the sum of inversion numbers of all 2^N resulting permutations, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc228_c`](../../analysis/AtCoder-arc228_c.md) | C - Partially Sort | 2971 | Given a permutation P of length N, for each of the 2^N subsequences, sort the elements in the subsequence in place while... |
