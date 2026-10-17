# Ternary Search

**Taxonomy Path**: `Miscellaneous` > `Search Techniques` > `Ternary Search`

## Description
This topic focuses on ternary search techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For each coordinate axis, points move with velocity +1, -1, or 0. The maximum coordinate x_max(t) is the upper envelope of at most 3 linear functions, and x_min(t) is the lower envelope of at most 3 linear functions. Thus, X(t) = x_max(t) - x_min(t) is a convex piecewise linear function with at most 6 slope changes. The same holds for Y(t). The product f(t) = X(t) * Y(t) is piecewise quadratic on each interval between breakpoints. The minimum can only occur at t = 0, at breakpoints where envelope lines intersect, or at the vertex of a convex quadratic segment, which can be found via ternary search on each interval.
- Common Reductions: Find the minimum bounding box area (x_max - x_min) * (y_max - y_min) over all times t >= 0 for N points moving at unit speed in orthogonal directions.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc130_f`](../../analysis/AtCoder-abc130_f.md) | Minimum Bounding Box | 2240 | Find the minimum bounding box area (x_max - x_min) * (y_max - y_min) over all times t >= 0 for N points moving at unit s... |
