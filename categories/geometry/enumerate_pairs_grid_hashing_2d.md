# Points, Vectors, Transformations, Dot Products, Cross Products, Precision Issues and Polar Sort(2D)

**Taxonomy Path**: `Geometry` > `Geometry 2D` > `Points, Vectors, Transformations, Dot Products, Cross Products, Precision Issues and Polar Sort(2D)`

## Description
This topic focuses on points, vectors, transformations, dot products, cross products, precision issues and polar sort(2d) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Fixed-radius near neighbors problem in 2D. Partition the plane into square grid cells of side length $K$. Any two points within distance $K$ must reside in the same cell or in adjacent cells. Checking pairs within each cell and against 4 canonical neighboring cells checks every candidate pair exactly once without false misses.
- Common Reductions: Enumerate all pairs of points $(i, j)$ with $i < j$ whose Euclidean distance is $\le K$. The number of such pairs is guaranteed to be $\le 4 \times 10^5$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc234_h`](../../analysis/AtCoder-abc234_h.md) | Ex. Enumerate Pairs | 2505 | Enumerate all pairs of points $(i, j)$ with $i < j$ whose Euclidean distance is $\le K$. The number of such pairs is gua... |
