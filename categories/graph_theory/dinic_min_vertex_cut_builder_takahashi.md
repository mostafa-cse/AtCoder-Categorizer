# Maximum Flow / Minimum Cut

**Taxonomy Path**: `Graph Theory` > `Flow and Min Cut` > `Maximum Flow / Minimum Cut`

## Description
This topic focuses on maximum flow / minimum cut techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Standard minimum vertex cut reduces to minimum edge cut via vertex splitting. Each vertex v is split into v_in and v_out with capacity c_v. Undirected edge (u, v) becomes infinite capacity directed edges u_out -> v_in and v_out -> u_in. Reconstructing cut vertices corresponds to saturated split edges where v_in is reachable from source in the residual graph and v_out is unreachable.
- Common Reductions: Find the minimum cost set of vertices to remove in an undirected graph with N <= 100 vertices and M <= 300 edges to disconnect vertex 1 from vertex N, and output the vertices removed.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc239_g`](../../analysis/AtCoder-abc239_g.md) | Builder Takahashi | 2215 | Find the minimum cost set of vertices to remove in an undirected graph with N <= 100 vertices and M <= 300 edges to disc... |
