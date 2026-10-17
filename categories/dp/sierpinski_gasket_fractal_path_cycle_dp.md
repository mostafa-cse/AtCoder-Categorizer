# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A Level $k$ Sierpinski gasket consists of 3 Level $(k-1)$ sub-gaskets meeting at 3 contact vertices. Any simple cycle is either entirely inside one of the 3 sub-gaskets, or visits all 3 sub-gaskets by traversing a path between the contact vertices in each sub-gasket.
Maintaining $a_k$ (paths between two corners not touching the third corner), $b_k$ (paths touching the third corner), and $c_k$ (cycles) yields exact closed-form recurrences: $c_k = 3 c_{k-1} + (a_{k-1} + b_{k-1})^3$, $b_k = b_{k-1} (a_{k-1}^2 + 2 a_{k-1} b_{k-1})$, $a_k = (a_{k-1} + b_{k-1})^2 + a_{k-1} (a_{k-1}^2 + 2 a_{k-1} b_{k-1})$.
- Common Reductions: Count the number of simple polygons (cycles) formed by the line segments of a Level $L$ Sierpinski gasket modulo $10^9+7$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc037_d`](../../analysis/AtCoder-arc037_d.md) | D. Chaotic Polygons | 2258 | Count the number of simple polygons (cycles) formed by the line segments of a Level $L$ Sierpinski gasket modulo $10^9+7... |
