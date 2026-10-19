# DP on Convex Hulls

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Convex Hulls`

## Description
This topic focuses on dp on convex hulls techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By Pick's theorem, 2 * Area of any integer polygon is an integer, so the area is an integer iff 2 * Area == 0 (mod 2). Fix the bottom-leftmost vertex P0 of the convex hull. Sort all other points radially around P0. A convex polygon rooted at P0 is formed by a counter-clockwise sequence of points P0 -> P_i1 -> P_i2 -> ... -> P0. Points strictly inside the polygon can be either included or excluded in S arbitrarily without affecting conv(S), contributing a factor of 2^{interior points}. The quantity 2 * Area (mod 2) accumulates additively as cross products of successive triangles.
- Common Reductions: Given N points in general position in the 2D plane, count the number of subsets S of size >= 3 whose convex hull conv(S) has an integer area, modulo 10^9 + 7.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc202_f`](../../analysis/AtCoder-abc202_f.md) | F. Integer Convex Hull | 2905 | Given N points in general position in the 2D plane, count the number of subsets S of size >= 3 whose convex hull conv(S)... |
