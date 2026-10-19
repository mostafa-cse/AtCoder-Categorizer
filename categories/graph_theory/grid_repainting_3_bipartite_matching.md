# Bipartite Matching (HopCroft Karp Algorithm and Kuhn's Algorithm)

**Taxonomy Path**: `Graph Theory` > `Matching` > `Bipartite Matching (HopCroft Karp Algorithm and Kuhn's Algorithm)`

## Description
This topic focuses on bipartite matching (hopcroft karp algorithm and kuhn's algorithm) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Construct a bipartite graph with row vertices 1..H on the left and column vertices 1..W on the right, where each red cell (r, c) represents an edge between row r and column c. For each connected component with V_R row vertices and V_C column vertices, we can find a spanning tree of V_R + V_C - 1 edges. By rooting the spanning tree at either a row vertex or a column vertex and processing edges bottom-up (leaves to root), we can eliminate either V_R - 1 rows and V_C columns (root at row), or V_R rows and V_C - 1 columns (root at column). In both choices, every processed edge connects a leaf to its parent, guaranteeing that the chosen cell is still red at the moment of the operation. Maximizing the total white area corresponds to minimizing (H - U)(W - V), which can be optimized over the number of components rooted at rows vs columns in O(K) time.
- Common Reductions: We are given an H x W grid with 'R' (red) and 'B' (blue) cells. In each step, we can choose a red cell and repaint its entire row white (Operation X), or choose a red cell and repaint its entire column white (Operation Y). Once a cell is white, it can no longer be chosen. We want to maximize the final number of white squares and output an optimal sequence of operations.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc119_d`](../../analysis/AtCoder-arc119_d.md) | D - Grid Repainting 3 | 2713 | We are given an H x W grid with 'R' (red) and 'B' (blue) cells. In each step, we can choose a red cell and repaint its e... |
