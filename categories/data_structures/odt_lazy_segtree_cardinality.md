# Segment Tree with Lazy Propagation

**Taxonomy Path**: `Data Structures (DS)` > `Segment Tree` > `Segment Tree with Lazy Propagation`

## Description
This topic focuses on segment tree with lazy propagation techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Since values $x \in [1, 60]$ are bounded, maintain 60 independent interval sets (ODT) for presence of each $x$. Adding $x$ to $[L, R]$ identifies subsegments where $x$ was absent, adding $+1$ to those subsegments and inserting them into the ODT. Deleting $x$ identifies subsegments where $x$ was present, adding $-1$ and removing them. A lazy segment tree maintains range maximum cardinality and frequency count.
- Common Reductions: Maintain sets $S_1, \dots, S_N$ under range insertions/deletions of $x \in [1, 60]$ and query range max cardinality and count. Maintaining 60 ODT interval sets and mapping additions/removals to a lazy segment tree answers all queries in $O(Q \log N)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc430_g`](../../analysis/AtCoder-abc430_g.md) | G. Range Set Modifying Query | 2371 | Maintain sets $S_1, \dots, S_N$ under range insertions/deletions of $x \in [1, 60]$ and query range max cardinality and ... |
