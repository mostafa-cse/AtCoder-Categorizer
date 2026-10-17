# 2D Prefix Sum

**Taxonomy Path**: `Basics` > `2D Prefix Sum` > `2D Prefix Sum`

## Description
This topic focuses on 2d prefix sum techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any two disjoint axis-aligned rectangles can be separated by either a horizontal dividing line (one rectangle in rows <= r, the other in rows > r) or a vertical dividing line (one in columns <= c, the other in columns > c). For every pair of rows (r1, r2), Kadane's algorithm on column sums finds the maximum subrectangle spanning those rows in O(W). Running prefix and suffix dynamic programming over row and column boundaries solves the problem in O(H^2 W + H W^2).
- Common Reductions: Find the maximum possible sum of two disjoint subrectangles in an H x W grid with H, W <= 300.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-dwango2016qual_d`](../../analysis/AtCoder-dwango2016qual_d.md) | 庭園 | 2233 | Find the maximum possible sum of two disjoint subrectangles in an H x W grid with H, W <= 300.... |
