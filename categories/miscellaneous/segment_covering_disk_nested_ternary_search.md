# Ternary Search

**Taxonomy Path**: `Miscellaneous` > `Search Techniques` > `Ternary Search`

## Description
This topic focuses on ternary search techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For any fixed center (X, Y), the minimum radius required to touch all segments is R(X, Y) = max_i dist((X, Y), seg_i). The distance from a point to a line segment is a convex function of (X, Y). The upper envelope (maximum) of convex functions is strictly convex! Thus R(X, Y) is a convex function in both X and Y, permitting nested ternary search: outer ternary search on X in [-10^5, 10^5], inner ternary search on Y in [-10^5, 10^5].
- Common Reductions: Given N segments in the 2D plane, find the center (X, Y) of a disk of minimum radius R that intersects all N segments.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc314_h`](../../analysis/AtCoder-abc314_h.md) | H. Disk and Segments | 2938 | Given N segments in the 2D plane, find the center (X, Y) of a disk of minimum radius R that intersects all N segments.... |
