# Articulation Points and Block Cut Tree

**Taxonomy Path**: `Graph Theory` > `Graph Connectivity` > `Articulation Points and Block Cut Tree`

## Description
This topic focuses on articulation points and block cut tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Let C be the initial number of connected components of green cells. Removing a vertex u changes the number of components depending on its articulation status: an isolated vertex reduces components by 1; a non-articulation vertex leaves components unchanged (delta = 0); an articulation vertex splits its component into k >= 2 pieces (delta = k - 1). Using Tarjan's DFS tree, for root r, delta = children - 1; for non-root u, delta = count of DFS children v with low[v] >= tin[u].
- Common Reductions: Compute the expected number of connected components of green cells after turning one green cell chosen uniformly at random into red.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc334_g`](../../analysis/AtCoder-abc334_g.md) | Christmas Color Grid 2 | 2242 | Compute the expected number of connected components of green cells after turning one green cell chosen uniformly at rand... |
