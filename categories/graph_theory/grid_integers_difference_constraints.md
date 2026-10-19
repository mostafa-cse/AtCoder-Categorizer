# System Of Difference Constraints

**Taxonomy Path**: `Graph Theory` > `Satisfiability` > `System Of Difference Constraints`

## Description
This topic focuses on system of difference constraints techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In each connected component of the bipartite graph between row nodes and column nodes, setting a reference potential determines all other potentials. If any cycle produces conflicting potentials, no solution exists. A valid non-negative assignment exists iff each component satisfies min_{r in K} x_r + min_{c in K} y_c >= 0.
- Common Reductions: Fill an R x C grid with non-negative integers such that every 2 x 2 subgrid satisfies a_{i, j} + a_{i+1, j+1} = a_{i, j+1} + a_{i+1, j}. This condition holds iff a_{i, j} = x_i + y_j for row potentials x_i and column potentials y_j. The given cells form edges in a bipartite graph with constraints x_i + y_j = a_k. Non-negativity requires min x_i + min y_j >= 0 in every connected component.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-codefestival_2016_qualA_d`](../../analysis/AtCoder-codefestival_2016_qualA_d.md) | Grid and Integers | 2684 | Fill an R x C grid with non-negative integers such that every 2 x 2 subgrid satisfies a_{i, j} + a_{i+1, j+1} = a_{i, j+... |
