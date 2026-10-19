# Min Cost Max Flow (MCMF)

**Taxonomy Path**: `Graph Theory` > `Flow and Min Cut` > `Min Cost Max Flow (MCMF)`

## Description
This topic focuses on min cost max flow (mcmf) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Bipartite graph between H rows and W columns. Each cell (r, c) with cost A_{r, c} is a directed edge r -> c with capacity infinity and cost A_{r, c}. Lower bounds of 1 on row and column coverage are handled via offset BIG. With successive shortest path MCMF, the optimal selection of cells is computed in polynomial time.
- Common Reductions: Color grid cells such that every row and every column has at least one colored cell, minimizing cost. This can be viewed as selecting a set of cells covering all rows and columns. We transform this into a Minimum Cost Maximum Flow problem: add a large base offset BIG to edges ensuring full coverage of rows and columns, then find the optimal flow with minimum cost using Primal-Dual / Successive Shortest Path algorithm.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc231_h`](../../analysis/AtCoder-abc231_h.md) | Minimum Coloring | 2681 | Color grid cells such that every row and every column has at least one colored cell, minimizing cost. This can be viewed... |
