# [Trick] Dijkstra on Segment Tree

**Taxonomy Path**: `Graph Theory` > `Shortest Paths` > `[Trick] Dijkstra on Segment Tree`

## Description
This topic focuses on [trick] dijkstra on segment tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each vertex $i$ only needs to connect to the smallest $B_j \ge (-A_i \bmod M)$ and to $B_{\pi_1}$ (the wrap-around point). Traveling clockwise along the cycle preserves the exact modular distances to all other $B_j$. From each cycle node, a 0-weight edge connects to the corresponding original vertex $j$. The resulting graph has $2N$ vertices and at most $4N$ edges, solved in $O(N \log N)$ using Dijkstra.
- Common Reductions: Find shortest path from 1 to $N$ on a directed complete graph where edge $i \to j$ has weight $(A_i + B_j) \bmod M$. Notice $(A_i + B_j) \bmod M = (B_j - (-A_i)) \bmod M$. This is exactly the clockwise distance on a cycle of length $M$ from coordinate $(-A_i) \bmod M$ to coordinate $B_j$! Instead of $N^2$ edges, place all $B_j$ on a cycle of $N$ nodes connected by their coordinate differences.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc232_g`](../../analysis/AtCoder-abc232_g.md) | G. Modulo Shortest Path | 2550 | Find shortest path from 1 to $N$ on a directed complete graph where edge $i \to j$ has weight $(A_i + B_j) \bmod M$. Not... |
