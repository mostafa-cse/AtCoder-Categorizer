# Segment Tree (Point Update Range Query)

**Taxonomy Path**: `Data Structures (DS)` > `Segment Tree` > `Segment Tree (Point Update Range Query)`

## Description
This topic focuses on segment tree (point update range query) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A column transition is represented by a 2^H x 2^H transfer matrix tracking which cells are covered by dominoes crossing into the next column. Since W <= 10^11 but only N <= 20000 columns are ever modified, the grid consists of K <= N modified columns interspersed with long contiguous blocks of empty columns. The matrix of an empty block of length L is M_0^L. Storing the 2K+1 matrix components in a segment tree allows O(log K * 4^3) point updates per query.
- Common Reductions: On an H x W grid (H in {1, 2}, W <= 10^11), N <= 20000 operations dynamically toggle caps on cells. After each operation, count the number of valid matchings (placing 0 or more dominoes on uncapped cells) modulo 10^9+7.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc025_4`](../../analysis/AtCoder-arc025_4.md) | D - コンセント | 2863 | On an H x W grid (H in {1, 2}, W <= 10^11), N <= 20000 operations dynamically toggle caps on cells. After each operation... |
