# Bipartite Matching (HopCroft Karp Algorithm and Kuhn's Algorithm)

**Taxonomy Path**: `Graph Theory` > `Matching` > `Bipartite Matching (HopCroft Karp Algorithm and Kuhn's Algorithm)`

## Description
This topic focuses on bipartite matching (hopcroft karp algorithm and kuhn's algorithm) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Slicing a block of dimensions X x Y x Z into 1x1x1 cubes requires (X-1) cuts along X, (Y-1) cuts along Y, and (Z-1) cuts along Z. However, cuts along two orthogonal axes can be grouped into independent slice operations: if a cut along dimension A and a cut along dimension B are executed together, they save 1 operation. This models a maximum matching on a bipartite graph where left vertices are cuts on one axis and right vertices are cuts on the orthogonal axis.
- Common Reductions: Given N rectangular prisms with dimensions (X_i, Y_i, Z_i), we can slice prisms along grid planes parallel to their faces into 1x1x1 unit cubes. Minimize the total number of cutting actions by sharing cuts between overlapping orthogonal dimensions via maximum bipartite matching.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc013_4`](../../analysis/AtCoder-arc013_4.md) | D. 切り分けできるかな？ (Can it be cut?) | 2535 | Given N rectangular prisms with dimensions (X_i, Y_i, Z_i), we can slice prisms along grid planes parallel to their face... |
