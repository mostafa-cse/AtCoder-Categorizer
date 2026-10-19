# Segment Tree (Point Update Range Query)

**Taxonomy Path**: `Data Structures (DS)` > `Segment Tree` > `Segment Tree (Point Update Range Query)`

## Description
This topic focuses on segment tree (point update range query) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Movement through concatenated rectangles is restricted to the shared vertical boundary intervals [0, min(H_i, H_{i+1})]. Each rectangle defines a piecewise linear transfer mapping reachable height intervals from its left boundary to its right boundary. Composing these interval maps forms an associative monoid. A Segment Tree maintaining composed interval transfer relations allows efficient point updates and range queries in O(log N) time.
- Common Reductions: Given N horizontally concatenated rectangles of dimensions H_i x W_i, process dynamic point updates and range reachability queries for paths traveling across rectangles [L, R].

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc179_e`](../../analysis/AtCoder-arc179_e.md) | E. Rectangle Concatenation | 2909 | Given N horizontally concatenated rectangles of dimensions H_i x W_i, process dynamic point updates and range reachabili... |
