# Topological Sorting

**Taxonomy Path**: `Graph Theory` > `Graph Traversal` > `Topological Sorting`

## Description
This topic focuses on topological sorting techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Edges (u, v) imply R_u <= R_v - 1 and L_v >= L_u + 1. Tightening bounds in reverse topological order propagates deadlines to predecessors. In unit-execution deadline scheduling on DAGs (Jackson's rule / EDF), assigning positions k = 1, 2, ..., N greedily to the available vertex with the earliest modified deadline R_u is optimal and solves the problem.
- Common Reductions: Given a directed graph of N vertices and M edges, find a permutation P satisfying P_u < P_v for all edges (u, v) and L_i <= P_i <= R_i for all i, or report impossible.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc304_h`](../../analysis/AtCoder-abc304_h.md) | Ex - Constrained Topological Sort | 2642 | Given a directed graph of N vertices and M edges, find a permutation P satisfying P_u < P_v for all edges (u, v) and L_i... |
