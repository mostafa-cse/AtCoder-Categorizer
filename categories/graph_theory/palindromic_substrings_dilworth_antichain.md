# POSET ft Dilworth's and Mirsky's Theorem

**Taxonomy Path**: `Graph Theory` > `Partially Ordered Set (POSET)` > `POSET ft Dilworth's and Mirsky's Theorem`

## Description
This topic focuses on poset ft dilworth's and mirsky's theorem techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A string of length N has at most N distinct palindromic substrings. Substring inclusion forms a partially ordered set (poset) on these palindromes. The problem seeks the maximum antichain of this poset. By Dilworth's Theorem, the maximum antichain size equals the minimum path cover of the comparability DAG, which is computed via maximum bipartite matching as |P| - max_matching.
- Common Reductions: Find the maximum size of a subset of distinct palindromic substrings of S such that no chosen substring is a substring of another chosen substring.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc237_h`](../../analysis/AtCoder-abc237_h.md) | Ex - Hakata | 2807 | Find the maximum size of a subset of distinct palindromic substrings of S such that no chosen substring is a substring o... |
