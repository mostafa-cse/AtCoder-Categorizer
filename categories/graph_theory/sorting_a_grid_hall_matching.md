# Halls Theorem

**Taxonomy Path**: `Graph Theory` > `Matching` > `Halls Theorem`

## Description
This topic focuses on halls theorem techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Target row of value v is tr(v) = (v - 1) / M. A bipartite graph with current rows on the left and target rows on the right has degree M for every vertex. By Hall's condition, every regular bipartite graph contains a perfect matching. Finding a matching via Kuhn's algorithm assigns one element per row to column col. Repeating M times completely constructs B. Sorting columns of B yields C, and sorting rows of C yields D.
- Common Reductions: Permute an N x M grid in 3 steps into sorted order D_{i, j} = (i - 1)M + j. Step 2 requires each column of B to contain exactly one element destined for each target row 0..N-1. Constructing matrix B column-by-column corresponds to finding M edge-disjoint 1-factors in an M-regular bipartite multigraph, guaranteed to exist by Hall's Marriage Theorem.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc037_d`](../../analysis/AtCoder-agc037_d.md) | Sorting a Grid | 2689 | Permute an N x M grid in 3 steps into sorted order D_{i, j} = (i - 1)M + j. Step 2 requires each column of B to contain ... |
