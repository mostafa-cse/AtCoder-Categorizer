# Centroid Decomposition

**Taxonomy Path**: `Data Structures (DS)` > `Centroid Decomposition` > `Centroid Decomposition`

## Description
This topic focuses on centroid decomposition techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In any Hamiltonian cycle on the complete graph, every edge e of the tree can be traversed at most 2 * min(sz_e, N - sz_e) times. Rooting the tree at its centroid allows achieving this upper bound for all edges simultaneously, so the maximum Hamiltonian cycle length is L_{cycle} = sum_e 2 * min(sz_e, N - sz_e) * weight(e). A Hamiltonian path is obtained by removing one edge from the cycle. If the tree has two centroids C_1 and C_2 (separated by an edge with sz = N/2), every step in the cycle must cross the centroid edge, so the minimum omitted edge has weight equal to that centroid edge. If the tree has a unique centroid C, the omitted edge can be the shortest edge incident to C.
- Common Reductions: Given a weighted tree of N vertices, construct a complete graph where the edge weight between u and v is their distance in the tree. Find the length of the longest Hamiltonian path in this complete graph.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc018_d`](../../analysis/AtCoder-agc018_d.md) | D - Tree and Hamilton Path | 2758 | Given a weighted tree of N vertices, construct a complete graph where the edge weight between u and v is their distance ... |
