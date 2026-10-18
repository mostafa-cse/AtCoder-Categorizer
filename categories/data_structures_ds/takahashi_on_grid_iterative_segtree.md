# Iterative Segment Tree

**Taxonomy Path**: `Data Structures (DS)` > `Segment Tree` > `Iterative Segment Tree`

## Description
This topic focuses on iterative segment tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: When moving from column $x$ to $x+1$, the vertical coordinate $y$ is clamped to $[L_{x+1}, U_{x+1}]$. Clamping functions $f(y) = \text{clamp}(y, f_L, f_U)$ and cost functions $g(y) = C + \max(y, g_L) - \min(y, g_U)$ form a monoid under composition. Thus, transitions across any range of columns can be composed and queried in $O(\log N)$ time using an Iterative Segment Tree.
- Common Reductions: Answer $Q$ distance queries on a grid where each column $x \in [1, N]$ has walkable vertical interval $[L_x, U_x]$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc365_f`](../../analysis/AtCoder-abc365_f.md) | F - Takahashi on Grid | 2561 | Answer $Q$ distance queries on a grid where each column $x \in [1, N]$ has walkable vertical interval $[L_x, U_x]$.... |
