# Maximum Flow / Minimum Cut

**Taxonomy Path**: `Graph Theory` > `Flow and Min Cut` > `Maximum Flow / Minimum Cut`

## Description
This topic focuses on maximum flow / minimum cut techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Construct a bipartite graph with N rows on the left and N values on the right. Each cell in row r with value v creates an edge (r, v). Since each row contains M values and each value appears M times across the grid, the bipartite multigraph is M-regular. By Hall's condition, every regular bipartite graph contains a 1-factor (perfect matching). Extracting this matching determines column j and leaves an (M-1)-regular bipartite graph. Repeating this M times completely factors the matrix.
- Common Reductions: By Hall's Marriage Theorem and the Birkhoff-von Neumann theorem, an N x M matrix where every integer 1..N appears exactly M times can be rearranged column-by-column into a Latin rectangle (where every column is a permutation of 1..N) by finding M successive perfect matchings in a regular bipartite graph.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc317_g`](../../analysis/AtCoder-abc317_g.md) | Rearranging | 2649 | By Hall's Marriage Theorem and the Birkhoff-von Neumann theorem, an N x M matrix where every integer 1..N appears exactl... |
