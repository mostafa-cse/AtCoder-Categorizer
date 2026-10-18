# Contribution Technique

**Taxonomy Path**: `Combinatorics` > `Techniques` > `Contribution Technique`

## Description
This topic focuses on contribution technique techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The area (X_max - X_min)(Y_max - Y_min) equals the number of unit cells [x, x+1] x [y, y+1] covered by the bounding box. A cell is covered iff the subset contains points both to its left and right, and both above and below. Decomposing by 4 quadrants around (x, y), the count of valid subsets is expressed via inclusion-exclusion in terms of quadrant counts. Sweeping across x and maintaining quadrant counts in a Lazy Segment Tree evaluates all contributions in O(N log N).
- Common Reductions: Given N points in the plane, compute the sum of bounding box areas (X_max - X_min)(Y_max - Y_min) over all non-empty subsets of points modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc201_e`](../../analysis/AtCoder-arc201_e.md) | E - Subsets and Bounding Box Areas | 2635 | Given N points in the plane, compute the sum of bounding box areas (X_max - X_min)(Y_max - Y_min) over all non-empty sub... |
