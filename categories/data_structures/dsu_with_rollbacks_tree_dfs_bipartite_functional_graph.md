# DSU with Rollbacks

**Taxonomy Path**: `Data Structures (DS)` > `Disjoint Set Union (DSU)` > `DSU with Rollbacks`

## Description
This topic focuses on dsu with rollbacks techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In any connected component of the value graph with V vertices and E edges, the maximum number of distinct vertices that can be covered by orienting edges is min(V, E). A tree component yields E = V-1, while any component containing a cycle yields all V vertices.
- Common Reductions: Along each tree path from 1 to v, select one of two balls (A_u, B_u) at each node to maximize distinct values. Model ball pairs as edges in a functional component graph and maintain the maximum matching across DFS paths using DSU with Rollbacks.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc302_h`](../../analysis/AtCoder-abc302_h.md) | Ex. Ball Collector | 2407 | Along each tree path from 1 to v, select one of two balls (A_u, B_u) at each node to maximize distinct values. Model bal... |
