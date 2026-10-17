# Dijkstra's Algorithm

**Taxonomy Path**: `Graph Theory` > `Shortest Paths` > `Dijkstra's Algorithm`

## Description
This topic focuses on dijkstra's algorithm techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Using $k$ Type B edges incurs quadratic cost $k(k+1)/2$. Since any simple Type A path costs $< N$, taking more than $\sqrt{2N} \approx 141$ Type B edges cannot compensate for Type A savings. For $k < B$, we maintain exact Type A cost $dist[u][k]$; for $k \ge B$, only the minimum $k$ is needed.
- Common Reductions: In a graph with Type A edges (cost 1) and Type B edges (the $k$-th traversed Type B edge costs $k$), find the minimum cost path from vertex 0 to all other vertices.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc052_c`](../../analysis/AtCoder-arc052_c.md) | C. 高橋くんと不思議な道 | 2277 | In a graph with Type A edges (cost 1) and Type B edges (the $k$-th traversed Type B edge costs $k$), find the minimum co... |
