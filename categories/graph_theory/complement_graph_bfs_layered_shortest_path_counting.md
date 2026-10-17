# Breadth First Search (BFS)

**Taxonomy Path**: `Graph Theory` > `Graph Traversal` > `Breadth First Search (BFS)`

## Description
This topic focuses on breadth first search (bfs) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Explicitly representing the complement graph takes O(N^2) time. Maintaining unvisited vertices in an std::set allows finding all unvisited non-deleted neighbors of u in O((deg_del(u) + 1) log N) time, totaling O((N + M) log N) for the BFS. In the resulting DAG of shortest paths, dp[v] = sum_{u in L_{d-1}} dp[u] - sum_{u in L_{d-1}, (u, v) in E_del} dp[u], computable in O(N + M) time.
- Common Reductions: Given a complete graph with N vertices from which M edges are deleted, find the number of shortest paths from 1 to N modulo 998244353. Complement-graph BFS finds distance layers, and layer DP counts paths by subtracting deleted edge transitions.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc319_g`](../../analysis/AtCoder-abc319_g.md) | G. Counting Shortest Paths | 2185 | Given a complete graph with N vertices from which M edges are deleted, find the number of shortest paths from 1 to N mod... |
