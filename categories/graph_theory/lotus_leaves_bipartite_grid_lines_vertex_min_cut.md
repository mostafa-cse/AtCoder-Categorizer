# Maximum Flow / Minimum Cut

**Taxonomy Path**: `Graph Theory` > `Flow and Min Cut` > `Maximum Flow / Minimum Cut`

## Description
This topic focuses on maximum flow / minimum cut techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Jumping along the same row or column corresponds to moving along row vertices R_i and column vertices C_j. A leaf at (i, j) connects row R_i and column C_j. Removing a leaf removes the incidence edge between R_i and C_j. S and T define source and sink row/column endpoints.
- Common Reductions: Minimum vertex cut on bipartite row/column incidence graph solved via Dinic maximum flow.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc074_d`](../../analysis/AtCoder-arc074_d.md) | Lotus Leaves | 2208 | Minimum vertex cut on bipartite row/column incidence graph solved via Dinic maximum flow.... |
