# Duality in Linear Programming (LP <> Flow)

**Taxonomy Path**: `Math` > `Mathematical Optimization` > `Duality in Linear Programming (LP <> Flow)`

## Description
This topic focuses on duality in linear programming (lp <> flow) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: This is an integer linear program on a bipartite graph. Because the constraint matrix is totally unimodular, the LP relaxation has integral optimal solutions. The LP dual corresponds to Minimum Cost Maximum Flow (MCMF) / circulation on a network with source S and sink T, where vertex costs and edge weights become capacities and costs. Successive Shortest Path / SPFA solves the dual directly.
- Common Reductions: On a bipartite graph with vertex sets L and R, placing a camera at u in L costs A_u with capacity C_u; at v in R costs B_v with capacity D_v. Edge (u, v) yields profit W_e if covered by either endpoint. Maximize net profit.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc224_h`](../../analysis/AtCoder-abc224_h.md) | H. Security Camera 2 | 2887 | On a bipartite graph with vertex sets L and R, placing a camera at u in L costs A_u with capacity C_u; at v in R costs B... |
