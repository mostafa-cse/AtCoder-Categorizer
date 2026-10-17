# BIT / Fenwick Tree

**Taxonomy Path**: `Data Structures (DS)` > `Binary Indexed Tree (BIT)` > `BIT / Fenwick Tree`

## Description
This topic focuses on bit / fenwick tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Define dummy boundary values A_0 = 0 and A_{N+1} = N+1. Transition from index i to j requires prev[A_j] <= i < j and next[A_i] > j. At any step j, only the most recent occurrence of each value satisfies next[i] >= j. Maintaining these active DP values in a Fenwick tree allows querying dp[j] = query(prev[A_j], j - 1), removing prev[A_j] from the BIT, and inserting j.
- Common Reductions: Count non-empty subsequences s of A that can be extracted in exactly one unique way as an index sequence modulo 998244353. A subsequence index sequence is unique iff between any two consecutive chosen indices x_i and x_{i+1}, neither A_{x_i} nor A_{x_{i+1}} appears.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc125_d`](../../analysis/AtCoder-arc125_d.md) | D. Unique Subsequence | 2187 | Count non-empty subsequences s of A that can be extracted in exactly one unique way as an index sequence modulo 99824435... |
