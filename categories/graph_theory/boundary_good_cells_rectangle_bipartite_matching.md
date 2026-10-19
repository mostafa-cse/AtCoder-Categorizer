# Bipartite Matching (HopCroft Karp Algorithm and Kuhn's Algorithm)

**Taxonomy Path**: `Graph Theory` > `Matching` > `Bipartite Matching (HopCroft Karp Algorithm and Kuhn's Algorithm)`

## Description
This topic focuses on bipartite matching (hopcroft karp algorithm and kuhn's algorithm) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: To achieve the global minimum colored area, operations must avoid spreading black cells across both dimensions. Minimum area is attained when all colored rectangles degenerate or align along minimal boundary strips. The legal pairings of boundary cells that preserve this minimal area partition naturally into bipartite compatible sets between opposing or adjacent boundary sections. Finding the maximum weight set of valid non-overlapping pairs reduces to Maximum Weight Matching on a Bipartite Graph.
- Common Reductions: On an N x N grid with weighted non-corner boundary cells, repeatedly choose two unused boundary cells and color the bounding rectangle black. Maximize the total sum of chosen cell weights such that the final colored black area is minimized.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc206_e`](../../analysis/AtCoder-arc206_e.md) | E. Rectangle Coloring | 2902 | On an N x N grid with weighted non-corner boundary cells, repeatedly choose two unused boundary cells and color the boun... |
