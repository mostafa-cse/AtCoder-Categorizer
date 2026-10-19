# Permutations, Combinations and Basic Counting Problems

**Taxonomy Path**: `Basics` > `Basic Counting` > `Permutations, Combinations and Basic Counting Problems`

## Description
This topic focuses on permutations, combinations and basic counting problems techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By shifting the entire set so that one string is 0^N, all strings in the set must have popcount <= 2, and the Hamming distance between any two strings must be <= 2. The intersection graph of pairs of bits forms a family of sets of size <= 2. There are only two geometric configurations that satisfy pairwise distance <= 2: (1) a star graph (all pairs share a common coordinate bit), or (2) a triangle of size 3 (three 2-element sets on 3 coordinates), plus singleton elements. By classifying the configuration into star-type families and small cliques (triangles, 4-cliques), each case can be counted independently using binomial coefficients.
- Common Reductions: Given N and K, count the number of subsets of size K of binary strings of length N such that every pair of strings in the subset has Hamming distance at most 2, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc200_e`](../../analysis/AtCoder-arc200_e.md) | E - popcount <= 2 | 2852 | Given N and K, count the number of subsets of size K of binary strings of length N such that every pair of strings in th... |
