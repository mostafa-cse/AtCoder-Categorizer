# DFS Tree

**Taxonomy Path**: `Graph Theory` > `Graph Traversal` > `DFS Tree`

## Description
This topic focuses on dfs tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In any connected component with $V$ vertices and $E$ edges, for any fixed subset of non-tree edges and any subset of vertices $S$ with $|S|$ even, there exists a unique subset of spanning tree edges yielding odd degrees exactly at $S$.
- Common Reductions: Given an undirected graph of $N$ vertices and $M$ edges, for each $k = 0, \dots, N$, count the number of spanning subgraphs having exactly $k$ vertices of odd degree, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc115_d`](../../analysis/AtCoder-arc115_d.md) | D. Odd Degree | 2325 | Given an undirected graph of $N$ vertices and $M$ edges, for each $k = 0, \dots, N$, count the number of spanning subgra... |
