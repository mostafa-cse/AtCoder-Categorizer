# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Assigning all edges $(i, j)$ ($i < j$) incident to vertex $j$ the same color $C_j$ guarantees that every triangle $(a, b, c)$ with $a < b < c$ has edges $(a, c)$ and $(b, c)$ of color $C_c$, completely preventing trichromatic triangles.
- Common Reductions: Given $N$, color the edges of the complete graph $K_N$ with three colors (Red, Blue, White) such that each color appears on exactly $M/3$ edges and no triangle contains all three colors, or determine impossible.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc131_e`](../../analysis/AtCoder-arc131_e.md) | E. Christmas Wreath | 2314 | Given $N$, color the edges of the complete graph $K_N$ with three colors (Red, Blue, White) such that each color appears... |
