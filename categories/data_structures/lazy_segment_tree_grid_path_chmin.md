# Segment Tree with Lazy Propagation

**Taxonomy Path**: `Data Structures (DS)` > `Segment Tree` > `Segment Tree with Lazy Propagation`

## Description
This topic focuses on segment tree with lazy propagation techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In an $(H+1) \times W$ grid, moving downwards increases moves by 1 everywhere. Blocking interval $[A_i, B_i]$ forces paths ending in $[A_i, B_i]$ to detour rightwards to $B_i + 1$, transforming reaching costs in $[A_i, B_i]$ into a single minimum detour candidate placed at $B_i + 1$. Maintaining values with lazy segment tree and a multiset provides running global minima in $O(\log W)$ per row.
- Common Reductions: In an $(H+1) \times W$ grid where each row $i$ has an impassable block $[A_i, B_i]$, find the minimum path length from row 1 to row $i+1$ moving only down or right for each $i = 1, \dots, H$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc177_f`](../../analysis/AtCoder-abc177_f.md) | F. I hate Shortest Path Problem | 2291 | In an $(H+1) \times W$ grid where each row $i$ has an impassable block $[A_i, B_i]$, find the minimum path length from r... |
