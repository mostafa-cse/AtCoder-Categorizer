# Sweep Line Algorithm and Radial Sweep

**Taxonomy Path**: `Geometry` > `Sweep Line` > `Sweep Line Algorithm and Radial Sweep`

## Description
This topic focuses on sweep line algorithm and radial sweep techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Rotate coordinates 45 degrees: (X, Y) = (x + y, x - y), so Manhattan distance becomes Chebyshev distance max(|X_1 - X_2|, |Y_1 - Y_2|) = D. Vertices reachable by the compass are exactly the connected component of {a, b} in the distance-D graph. To run BFS in O(N log N) time, store unvisited points in balanced BSTs ordered by X and Y; deleting visited points ensures each vertex is visited once. Counting distance-D pairs in the component uses binary search on 1D slices.
- Common Reductions: N points on the plane. A Manhattan compass points to a pair of points with fixed distance D = d(a, b). Compass can move from (p, q) to (p, r) if d(p, r) == d(p, q) == D. Find the number of reachable pairs.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc065_c`](../../analysis/AtCoder-arc065_c.md) | E - Manhattan Compass | 2835 | N points on the plane. A Manhattan compass points to a pair of points with fixed distance D = d(a, b). Compass can move ... |
