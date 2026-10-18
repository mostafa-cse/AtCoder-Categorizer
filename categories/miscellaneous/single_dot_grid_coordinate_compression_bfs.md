# Coordinate Compression

**Taxonomy Path**: `Miscellaneous` > `Techniques` > `Coordinate Compression`

## Description
This topic focuses on coordinate compression techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because (0, 0) does not lie on any segment, the cow can enter all 4 adjacent open quadrants around the origin. Adjacent compressed faces share open boundaries unless blocked by a segment spanning that coordinate interval. Unbounded components reach the outer coordinate boundary.
- Common Reductions: Compute the reachable area of a cow starting at $(0, 0)$ bounded by $N$ vertical and $M$ horizontal segments. Perform 2D coordinate compression on all segment endpoints and 0, forming an $O(N + M) \times O(N + M)$ grid of rectangular faces. Mark wall boundaries between adjacent cells and run BFS from $(0, 0)$. If the search escapes the outer bounding box, output 'INF'; otherwise, sum the exact rectangular areas.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc168_f`](../../analysis/AtCoder-abc168_f.md) | F. . Single Dot | 2478 | Compute the reachable area of a cow starting at $(0, 0)$ bounded by $N$ vertical and $M$ horizontal segments. Perform 2D... |
