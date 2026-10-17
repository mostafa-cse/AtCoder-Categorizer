# Depth First Search (DFS)

**Taxonomy Path**: `Graph Theory` > `Graph Traversal` > `Depth First Search (DFS)`

## Description
This topic focuses on depth first search (dfs) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Traversing a spanning tree from root 1, edge x_u + x_v = s implies x_v = -sgn[u]*t + (s - C[u]), forcing sgn[v] = -sgn[u]. Non-tree edges between same-sign vertices form an odd cycle: sgn[u]*t + C[u] + sgn[v]*t + C[v] = s, uniquely solving for t. Non-tree edges between opposite-sign vertices must satisfy C[u] + C[v] = s. For bipartite graphs, x_v >= 1 imposes lower bounds t >= 1 - C[v] (when sgn = +1) and upper bounds t <= C[v] - 1 (when sgn = -1).
- Common Reductions: Determine the number of positive integer vertex labelings on a connected graph such that for every edge (u, v), x_u + x_v = s_e. Fix x_1 = t. Every vertex value x_v is parameterized as sgn[v] * t + C[v]. An odd cycle produces an equation fixing t to a unique integer; a bipartite graph yields a continuous bounding interval [t_min, t_max] of valid positive integers.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-soundhound2018_summer_qual_e`](../../analysis/AtCoder-soundhound2018_summer_qual_e.md) | E. + Graph | 2164 | Determine the number of positive integer vertex labelings on a connected graph such that for every edge (u, v), x_u + x_... |
