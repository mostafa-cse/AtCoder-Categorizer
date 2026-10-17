# Interval DP / Range DP / Matrix Chain Multiplication (MCM)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Classic DP` > `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`

## Description
This topic focuses on interval dp / range dp / matrix chain multiplication (mcm) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: All strings having equal length $M$ implies integer order coincides with lexicographical order. When strings $S_l \dots S_r$ share a common prefix up to column $j-1$, their $j$-th characters must form a non-decreasing sequence of digits $d \in [0, 9]$, partitioning $[l, r]$ into subsegments that recurse independently on column $j+1$.
- Common Reductions: Given $N$ strings of length $M$ with digits and `?`, count completions such that $S_1 < S_2 < \dots < S_N$ as integers. Equal string lengths equate integer order with lexicographical order, solved by interval DP partitioning into non-decreasing digit blocks in $O(N^3 M \cdot 10)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc292_g`](../../analysis/AtCoder-abc292_g.md) | G. Count Substrings | 2340 | Given $N$ strings of length $M$ with digits and `?`, count completions such that $S_1 < S_2 < \dots < S_N$ as integers. ... |
