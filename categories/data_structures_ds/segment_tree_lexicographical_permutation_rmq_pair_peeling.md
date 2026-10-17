# Segment Tree (Point Update Range Query)

**Taxonomy Path**: `Data Structures (DS)` > `Segment Tree` > `Segment Tree (Point Update Range Query)`

## Description
This topic focuses on segment tree (point update range query) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In any sequence of adjacent pair removals, every removed pair $(x, y)$ originally occupied an even-length interval between them and had alternating parities relative to the subarray boundary. The problem greedily decouples into independent even-length subsegments $[l, pos(x)-1]$, $[pos(x)+1, pos(y)-1]$, and $[pos(y)+1, r]$ managed by a priority queue.
- Common Reductions: Given a permutation $P$ of length $2N$, repeatedly select an adjacent pair $(P_i, P_{i+1})$ in the current sequence to place at the front of a new sequence, prioritizing lexicographically smallest sequences. Find the resulting permutation.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc080_c`](../../analysis/AtCoder-arc080_c.md) | E. Young Maids | 2277 | Given a permutation $P$ of length $2N$, repeatedly select an adjacent pair $(P_i, P_{i+1})$ in the current sequence to p... |
