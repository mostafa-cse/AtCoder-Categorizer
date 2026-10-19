# Dynamic Convex Hull

**Taxonomy Path**: `Geometry` > `Convex Polygon` > `Dynamic Convex Hull`

## Description
This topic focuses on dynamic convex hull techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Maximizing a linear function A x + B y over a set of points corresponds to finding extreme vertices on the upper/lower convex hull. Because points are added dynamically, offline CDQ divide-and-conquer can process insertions in the left half and answer queries in the right half via ternary search / two pointers on the static convex hull in O(Q log^2 Q) time.
- Common Reductions: Process Q operations online: add point (X_i, Y_i) to set S, or query max_{(x, y) in S} (A_i x + B_i y).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc244_h`](../../analysis/AtCoder-abc244_h.md) | Ex. Linear Maximization | 2878 | Process Q operations online: add point (X_i, Y_i) to set S, or query max_{(x, y) in S} (A_i x + B_i y).... |
