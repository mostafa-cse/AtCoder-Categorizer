# Stack

**Taxonomy Path**: `Basics` > `Standard Template Library (STL)` > `Stack`

## Description
This topic focuses on stack techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Curves with at least one internal endpoint never form boundary-to-boundary cuts and can always be routed around each other in 2D space. Boundary-to-boundary curves form chords of the rectangle disk. Two chords intersect if and only if their endpoints alternate along the perimeter. Mapping perimeter coordinates clockwise to 1D and checking matching pairs via a stack resolves the question in O(N log N) time.
- Common Reductions: Determine if N pairs of numbered points in an R x C rectangle can be connected by non-intersecting continuous curves inside the rectangle. Only pairs where both endpoints lie on the boundary can partition the rectangle; internal points can always be routed freely.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc076_c`](../../analysis/AtCoder-arc076_c.md) | E. Connected? | 2180 | Determine if N pairs of numbered points in an R x C rectangle can be connected by non-intersecting continuous curves ins... |
