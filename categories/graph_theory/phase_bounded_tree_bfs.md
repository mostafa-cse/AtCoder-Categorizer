# Breadth First Search (BFS)

**Taxonomy Path**: `Graph Theory` > `Graph Traversal` > `Breadth First Search (BFS)`

## Description
This topic focuses on breadth first search (bfs) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Jumping distance $K$ in a tree can be modeled as taking $K$ tree steps without immediately traversing back along the entry edge. In BFS, each vertex $v$ at step phase $d \bmod K$ needs to be visited at most twice across different incoming edges; third and subsequent visits to the same vertex at the same phase provide no new unvisited outgoing transitions.
- Common Reductions: Find minimum tree jumps of length $K$ from vertex 1 to all vertices. BFS over $2(N-1)$ directed edges limits visits per vertex to at most 2 per phase $d \bmod K$, yielding optimal paths in $O(NK)$ time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc414_f`](../../analysis/AtCoder-abc414_f.md) | F. Jump Traveling | 2357 | Find minimum tree jumps of length $K$ from vertex 1 to all vertices. BFS over $2(N-1)$ directed edges limits visits per ... |
