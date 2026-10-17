# Suffix Array

**Taxonomy Path**: `Strings` > `Suffix Structures` > `Suffix Array`

## Description
This topic focuses on suffix array techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In the suffix array, LCP(S_i, S_j) is the range minimum of the LCP array between rank(i) and rank(j). The sum of range minimums from rank(i) to all other positions decomposes into left and right prefix contributions, efficiently computed in O(N) using monotonic stacks maintaining running aggregate sums.
- Common Reductions: Compute the sum of longest common prefixes between suffix S_i and all other suffixes S_j for every i in [1, N] for string S of length N <= 10^6.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc213_f`](../../analysis/AtCoder-abc213_f.md) | Common Prefixes | 2215 | Compute the sum of longest common prefixes between suffix S_i and all other suffixes S_j for every i in [1, N] for strin... |
