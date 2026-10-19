# Inclusion Exclusion on Multiples

**Taxonomy Path**: `Combinatorics` > `Inclusion Exclusion` > `Inclusion Exclusion on Multiples`

## Description
This topic focuses on inclusion exclusion on multiples techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The condition that all x_i are distinct can be inverted over the set partition lattice Pi_N using Möbius inversion. For any partition P of {1, ..., N}, setting all elements in block B to be equal means their common value is a multiple of lcm_{i in B}(D_i) <= M, giving floor(M / lcm(B)) choices. The Möbius weight of block B is (-1)^{|B|-1} (|B|-1)!. The problem reduces to finding the sum of products of block weights over all partitions of {1, ..., N}, which can be solved via subset DP / SOS convolution in O(3^N) time.
- Common Reductions: Given an array D of N integers and upper bound M, count sequences (x_1, ..., x_N) such that 1 <= x_i <= M, D_i divides x_i, and all x_i are pairwise distinct, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc236_h`](../../analysis/AtCoder-abc236_h.md) | Ex. Distinct Multiples | 2898 | Given an array D of N integers and upper bound M, count sequences (x_1, ..., x_N) such that 1 <= x_i <= M, D_i divides x... |
