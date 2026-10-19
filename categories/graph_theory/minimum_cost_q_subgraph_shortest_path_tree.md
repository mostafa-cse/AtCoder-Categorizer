# Dijkstra's Algorithm

**Taxonomy Path**: `Graph Theory` > `Shortest Paths` > `Dijkstra's Algorithm`

## Description
This topic focuses on dijkstra's algorithm techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A 'Q' subgraph consists of a simple cycle C and an edge (u, v) attached to the cycle, where u in C and v not in C. In any optimal configuration, the vertex u on the cycle has degree 3, and all other vertices on the cycle have degree 2. This is equivalent to finding a vertex u with degree >= 3, taking an edge (u, v) as the tail, and finding a simple cycle passing through u that does not use v. For each candidate degree-3 vertex u, we can remove its minimum incident edges or run shortest paths on the universal cover / Dijkstra to find the shortest cycle through u not containing v.
- Common Reductions: Given a weighted undirected graph, find the minimum total weight of a subgraph shaped like the letter 'Q': a simple cycle plus a path attached to the cycle, such that all vertices on the cycle and path are distinct.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc308_h`](../../analysis/AtCoder-abc308_h.md) | Ex - Make Q | 2861 | Given a weighted undirected graph, find the minimum total weight of a subgraph shaped like the letter 'Q': a simple cycl... |
