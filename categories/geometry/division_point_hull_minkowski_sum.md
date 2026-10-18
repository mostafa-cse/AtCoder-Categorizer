# Minkowski Sum

**Taxonomy Path**: `Geometry` > `Convex Polygon` > `Minkowski Sum`

## Description
This topic focuses on minkowski sum techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The set of all division points Q[l, r) on an interval [l, r) with midpoint m satisfies Q[l, r) = Q[l, m) U Q[m, r) U (q/(p+q) * P[l, m) + p/(p+q) * P[m, r)). Taking convex hulls on both sides: conv(Q[l, r)) = conv(conv(Q[l, m)) U conv(Q[m, r)) U (q * conv(P[l, m)) + p * conv(P[m, r)))). The Minkowski sum of two convex polygons of sizes A and B has size at most A + B and can be computed in linear time O(A + B) by merging edge vectors by polar angle. Across all levels of the divide-and-conquer tree, the total vertices processed is O(N log N), yielding an O(N log^2 N) algorithm.
- Common Reductions: Given N points P_1, ..., P_N and ratio p : q, each pair (i, j) with 1 <= i < j <= N generates a division point Q_{i,j} = (q * P_i + p * P_j) / (p + q). Find the area of the convex hull of all Q_{i,j}.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc478_g`](../../analysis/AtCoder-abc478_g.md) | G. Division Point Hull | 2582 | Given N points P_1, ..., P_N and ratio p : q, each pair (i, j) with 1 <= i < j <= N generates a division point Q_{i,j} =... |
