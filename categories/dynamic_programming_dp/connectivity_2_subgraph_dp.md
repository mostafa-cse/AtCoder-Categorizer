# Subset Convolution

**Taxonomy Path**: `Dynamic Programming (DP)` > `Bit Related DP` > `Subset Convolution`

## Description
This topic focuses on subset convolution techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For each vertex subset S, compute C[S] = number of connected subgraphs on S by subtracting non-connected subgraphs (partitioning on the connected component containing the lowest set bit of S). In the full graph, if S is the connected component containing vertex 1, all edges inside S are chosen in C[S] ways, edges in V \ S are chosen in 2^(e(V \ S)) ways, and no cross-edges exist. Summing over all S containing {1, k} gives the exact answer.
- Common Reductions: Count subgraphs where Vertex 1 is connected to Vertex k using connected component subset DP to enumerate connected induced subgraphs, then summing over all components containing both 1 and k.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc213_g`](../../analysis/AtCoder-abc213_g.md) | Connectivity 2 | 2663 | Count subgraphs where Vertex 1 is connected to Vertex k using connected component subset DP to enumerate connected induc... |
