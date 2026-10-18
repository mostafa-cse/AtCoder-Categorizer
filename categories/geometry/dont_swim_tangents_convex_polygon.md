# Tangents from Point to Convex and Convex to Convex(2D)

**Taxonomy Path**: `Geometry` > `Geometry 2D` > `Tangents from Point to Convex and Convex to Convex(2D)`

## Description
This topic focuses on tangents from point to convex and convex to convex(2d) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because the obstacle is a convex polygon, shortest paths that touch the obstacle must follow the boundary in either clockwise or counter-clockwise orientation between tangent points. For any external point $P$, there are exactly two tangent vertices to the convex polygon, found by finding the vertices that achieve the extreme cross-products (orientations) with respect to $P$. Connecting $S$'s tangents to $T$'s tangents along both perimeter paths yields at most 4 candidate routes.
- Common Reductions: Find the shortest path between $S$ and $T$ in 2D that does not enter the strict interior of a strictly convex polygon with $N$ vertices. If the straight line segment $ST$ does not intersect the polygon interior, the answer is simply the Euclidean distance $|ST|$. Otherwise, the shortest path must follow a tangent line from $S$ to some polygon vertex $V_i$, travel along the polygon perimeter, and leave via a tangent line from some polygon vertex $V_j$ to $T$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc286_h`](../../analysis/AtCoder-abc286_h.md) | Ex. Don't Swim | 2526 | Find the shortest path between $S$ and $T$ in 2D that does not enter the strict interior of a strictly convex polygon wi... |
