# Point in Convex Polygon in log(N)(2D)

**Taxonomy Path**: `Geometry` > `Geometry 2D` > `Point in Convex Polygon in log(N)(2D)`

## Description
This topic focuses on point in convex polygon in log(n)(2d) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A strictly convex N-gon with CCW vertices P_0, ..., P_{N-1} can be decomposed into N-2 triangular sectors originating from P_0. For any query point Q, check if it falls within the wedge between rays P_0->P_1 and P_0->P_{N-1}. If so, binary search in O(log N) on the sector index i in [1, N-2] where Q lies between ray P_0->P_i and P_0->P_{i+1}. Then test orientation of Q relative to the outer edge P_i->P_{i+1} using 2D cross products to classify as IN, ON, or OUT.
- Common Reductions: Determine whether each of Q query points lies strictly inside (IN), on the boundary (ON), or strictly outside (OUT) a strictly convex N-gon.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc296_g`](../../analysis/AtCoder-abc296_g.md) | Polygon and Points | 2241 | Determine whether each of Q query points lies strictly inside (IN), on the boundary (ON), or strictly outside (OUT) a st... |
