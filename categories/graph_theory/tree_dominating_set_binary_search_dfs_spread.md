# Depth First Search (DFS)

**Taxonomy Path**: `Graph Theory` > `Graph Traversal` > `Depth First Search (DFS)`

## Description
This topic focuses on depth first search (dfs) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Binary search on the answer T in [1, N]. The decision problem asks whether all vertices can be covered by <= K centers of radius T (Tree T-Dominating Set). In a rooted tree, a bottom-up post-order DFS greedily covers vertices: each node tracks max uncovered distance d and min center distance c in its subtree. If c + d <= T, the deepest uncovered vertex is covered by an existing center (d = -inf). If d == T, no ancestor can cover this deepest vertex, forcing a center at the current node.
- Common Reductions: Find the minimum time T for information to spread to all vertices of a tree from at most K chosen source vertices.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc116_e`](../../analysis/AtCoder-arc116_e.md) | Spread of Information | 2236 | Find the minimum time T for information to spread to all vertices of a tree from at most K chosen source vertices.... |
