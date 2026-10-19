# Dijkstra's Algorithm

**Taxonomy Path**: `Graph Theory` > `Shortest Paths` > `Dijkstra's Algorithm`

## Description
This topic focuses on dijkstra's algorithm techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any travel between houses through intermediate non-house vertices can be decomposed into transitions between Voronoi cells of houses. By running multi-source Dijkstra from all K houses simultaneously, each vertex v is assigned its closest house h(v) and distance d(v). For each edge (u, v) with cost c, traversing from h(u) to h(v) via edge (u, v) requires stamina d(u) + d(v) + c. This forms an auxiliary graph with at most M edges connecting the K houses. Answering reachability queries for stamina threshold t reduces to dynamic connectivity or Kruskal's MST on this auxiliary graph, solvable offline with DSU.
- Common Reductions: In a weighted undirected graph with N vertices, houses are located at vertices 1 through K. Takahashi can travel between houses with stamina limit t without resting at non-house vertices. For Q queries (x, y, t), determine if Takahashi can travel between house x and house y.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc250_h`](../../analysis/AtCoder-abc250_h.md) | Ex - Trespassing Takahashi | 2773 | In a weighted undirected graph with N vertices, houses are located at vertices 1 through K. Takahashi can travel between... |
