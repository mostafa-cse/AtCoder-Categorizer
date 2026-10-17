# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: N = 2 is impossible. For N = 3, quality 1 is achievable. For N = 4, 5, 6, 7, quality 3 is achievable using fixed base patterns. Since any N >= 4 can be decomposed as N = 4x + y with y in {4, 5, 6, 7}, tiling the grid with x blocks of size 4 and 1 block of size y along the main diagonal achieves uniform quality 3 across all rows and columns.
- Common Reductions: Place dominoes on an N x N grid such that every row and every column has the exact same quality Q >= 1 (number of covered squares by dominoes).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc041_c`](../../analysis/AtCoder-agc041_c.md) | Domino Quality | 2220 | Place dominoes on an N x N grid such that every row and every column has the exact same quality Q >= 1 (number of covere... |
