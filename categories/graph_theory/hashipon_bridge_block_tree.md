# Articulation Bridges and Bridge Tree

**Taxonomy Path**: `Graph Theory` > `Graph Connectivity` > `Articulation Bridges and Bridge Tree`

## Description
This topic focuses on articulation bridges and bridge tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A graph is 2-edge-connected if and only if it has no bridges. By finding all 2-edge-connected components (biconnected components via Tarjan or DFS bridge-finding algorithm) and contracting each component into a single vertex, the graph collapses into a bridge-block tree (2-edge-connected component tree). To make a tree 2-edge-connected by adding edges, the minimum number of edges needed is ceil(L / 2), where L is the number of leaves in the bridge-block tree.
- Common Reductions: Given an undirected connected graph G, find the minimum number of additional edges needed to make the entire graph 2-edge-connected (bridge-free).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-tenka1_2015_qualA_d`](../../analysis/AtCoder-tenka1_2015_qualA_d.md) | D. ハシポン (Hashipon) | 2559 | Given an undirected connected graph G, find the minimum number of additional edges needed to make the entire graph 2-edg... |
