# Divide and Conquer

**Taxonomy Path**: `Basics` > `Divide and Conquer` > `Divide and Conquer`

## Description
This topic focuses on divide and conquer techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: On a grid without obstacles, distance is L1 Manhattan distance |x1 - x2| + |y1 - y2|. Black squares form square obstacles of size 3^t for t in 0..30. A path between two points must detour around at most one maximal blocking obstacle of size 3^t at any level. The extra detour around an obstacle of size 3^t is 2 * min(min(x1%3^t, x2%3^t) + 1, 3^t - max(x1%3^t, x2%3^t)). The exact distance equals the Manhattan distance plus 2 * max(extra_x, extra_y).
- Common Reductions: Given a Level 30 Sierpinski carpet fractal of size 3^30 x 3^30 where center blocks of size 3^t x 3^t are solid black obstacles, answer Q queries finding the shortest path distance through white cells between (a, b) and (c, d).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-panasonic2020_f`](../../analysis/AtCoder-panasonic2020_f.md) | F - Fractal Shortest Path | 2834 | Given a Level 30 Sierpinski carpet fractal of size 3^30 x 3^30 where center blocks of size 3^t x 3^t are solid black obs... |
