# Duality in Linear Programming (LP <> Flow)

**Taxonomy Path**: `Math` > `Mathematical Optimization` > `Duality in Linear Programming (LP <> Flow)`

## Description
This topic focuses on duality in linear programming (lp <> flow) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Binary search on the target distance d. By LP duality, checking if shortest path distance >= d can be achieved is equivalent to finding potentials x_u in {0, ..., d} with x_1 = 0, x_N = d and x_v - x_u <= 1 such that sum_{(u, v)} [x_v - x_u = 1] <= K. This is a multi-label project selection (k-value min-cut) problem on a graph with N x d nodes, where difference constraints x_v - x_u <= 1 are infinity-capacity edges and unit penalties are capacity-1 edges.
- Common Reductions: In a directed graph with N vertices and M edges of weight 0, choose exactly K edges to set to weight 1 to maximize the shortest path distance from 1 to N.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc397_g`](../../analysis/AtCoder-abc397_g.md) | G. Maximize Distance | 2947 | In a directed graph with N vertices and M edges of weight 0, choose exactly K edges to set to weight 1 to maximize the s... |
