# Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum

**Taxonomy Path**: `Data Structures (DS)` > `Monotonic Data Structures` > `Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum`

## Description
This topic focuses on monotonic stack: all nearest smaller values and all subarray maximum/minimum techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Every removed cube strictly decreases the front and back painted area by 2, contributing $-2K$ to the total area change. Side area decreases by 2 only when a complete horizontal row across a contiguous peak between higher boundaries is shaved. A monotonic stack decomposes the histogram into peak blocks $(W_i, \Delta H_i)$, where width $W_i$ represents the number of cubes per shaved horizontal layer, giving an additional $-2$ area reduction per unit layer. Greedy allocation of $K$ to the narrowest widths $W_i$ first minimizes the final surface area.
- Common Reductions: Remove at most $K$ unit cubes from a 2D histogram of heights $A_i$ (keeping all $A_i \ge 1$) to minimize the total painted surface area.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-cf_2015_morning_hard_b`](../../analysis/AtCoder-cf_2015_morning_hard_b.md) | D - 立方体とペンキ | 2456 | Remove at most $K$ unit cubes from a 2D histogram of heights $A_i$ (keeping all $A_i \ge 1$) to minimize the total paint... |
