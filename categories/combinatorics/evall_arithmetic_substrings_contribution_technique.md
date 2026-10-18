# Contribution Technique

**Taxonomy Path**: `Combinatorics` > `Techniques` > `Contribution Technique`

## Description
This topic focuses on contribution technique techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any valid arithmetic substring decomposes into terms separated by '+', where each term is a product of numbers separated by '*'. Scanning $j$ linearly, maintain base sums from preceding '+' blocks, historical product sums $H$ within the current block, and suffix expansions of the current number in $O(1)$ per digit.
- Common Reductions: Evaluate all valid arithmetic substrings $S[i..j]$ consisting of digits, '+', and '*' and compute their total sum modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc338_g`](../../analysis/AtCoder-abc338_g.md) | G. evall | 2573 | Evaluate all valid arithmetic substrings $S[i..j]$ consisting of digits, '+', and '*' and compute their total sum modulo... |
