# Reachability Tree / DSU Tree / Kruskal Reconstruction Tree (KRT)

**Taxonomy Path**: `Data Structures (DS)` > `Disjoint Set Union (DSU)` > `Reachability Tree / DSU Tree / Kruskal Reconstruction Tree (KRT)`

## Description
This topic focuses on reachability tree / dsu tree / kruskal reconstruction tree (krt) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Bottleneck path distance between u and v is given by their LCA on the Kruskal Reconstruction Tree (KRT). Changing edge e's weight affects the distance iff e was a bottleneck bridge in the threshold graph at weight W. By building the KRT and maintaining 2-edge-connected components (2ECC bridge-block trees) layer-by-layer, we can detect whether alternative paths exist at weight W.
- Common Reductions: In a weighted undirected graph, process queries asking: if the weight of edge e is increased from w to w', how does the bottleneck shortest path distance between u and v change?

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc301_h`](../../analysis/AtCoder-abc301_h.md) | Ex. Difference of Distance | 2898 | In a weighted undirected graph, process queries asking: if the weight of edge e is increased from w to w', how does the ... |
