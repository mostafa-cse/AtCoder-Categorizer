# Dijkstra's Algorithm

**Taxonomy Path**: `Graph Theory` > `Shortest Paths` > `Dijkstra's Algorithm`

## Description
This topic focuses on dijkstra's algorithm techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Two travelers traveling at speed 1 along shortest paths of length $L$ can only collide at time $t = L/2$. The collision must occur at a unique location: either at a vertex with $2 \cdot d_S(v) = L$, or strictly inside an edge $(u, v)$ where $2 \cdot d_S(u) < L$ and $2 \cdot d_T(v) < L$.
- Common Reductions: Given an undirected weighted graph, Takahashi travels from $S$ to $T$ and Aoki from $T$ to $S$ along shortest paths at constant speed. Count pairs of shortest paths where they never meet (neither at a vertex nor along an edge), modulo $10^9+7$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc090_c`](../../analysis/AtCoder-arc090_c.md) | E. Avoiding Collision | 2319 | Given an undirected weighted graph, Takahashi travels from $S$ to $T$ and Aoki from $T$ to $S$ along shortest paths at c... |
