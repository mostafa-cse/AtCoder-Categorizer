# Convex Hull(2D)

**Taxonomy Path**: `Geometry` > `Geometry 2D` > `Convex Hull(2D)`

## Description
This topic focuses on convex hull(2d) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The average of A[k..r] is (S_r - S_{k-1}) / (r - (k - 1)), which is the slope between points (k - 1, S_{k-1}) and (r, S_r). Maximizing slope from (k - 1, S_{k-1}) to points to its right is equivalent to finding the tangent to the lower convex hull of { (j, S_j) : j >= k }.
- Common Reductions: Geometric slope interpretation of subsegment average as tangent to lower convex hull maintained via right-to-left monotonic stack.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc341_g`](../../analysis/AtCoder-abc341_g.md) | Highest Ratio | 2208 | Geometric slope interpretation of subsegment average as tangent to lower convex hull maintained via right-to-left monoto... |
