# Breadth First Search (BFS)

**Taxonomy Path**: `Graph Theory` > `Graph Traversal` > `Breadth First Search (BFS)`

## Description
This topic focuses on breadth first search (bfs) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each query $(i, j)$ computes the sum over $[j \cdot 2^i, (j+1) \cdot 2^i - 1]$, which is the prefix sum difference $P[(j+1) \cdot 2^i] - P[j \cdot 2^i]$. In the graph with vertices $0, \dots, 2^N$ and undirected edges between $j \cdot 2^i$ and $(j+1) \cdot 2^i$, the minimum query sequence to obtain $P[R+1] - P[L]$ is the shortest path between $L$ and $R+1$ found by BFS.
- Common Reductions: Given $N, L, R$, find $\sum_{k=L}^R A_k \bmod 100$ in at most 100 interactive queries of the form $(i, j)$ computing $\sum_{k=j \cdot 2^i}^{(j+1)2^i - 1} A_k \bmod 100$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc355_e`](../../analysis/AtCoder-abc355_e.md) | E. Guess the Sum | 2299 | Given $N, L, R$, find $\sum_{k=L}^R A_k \bmod 100$ in at most 100 interactive queries of the form $(i, j)$ computing $\s... |
