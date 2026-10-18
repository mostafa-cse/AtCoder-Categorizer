# Sweep Line Algorithm and Radial Sweep

**Taxonomy Path**: `Geometry` > `Sweep Line` > `Sweep Line Algorithm and Radial Sweep`

## Description
This topic focuses on sweep line algorithm and radial sweep techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Two intervals $(L, R)$ and $(l_i, r_i)$ intersect (with non-empty intersection and neither containing the other) iff either $L < l_i < R < r_i$ or $l_i < L < r_i < R$. In the $(L, R)$ plane, each given interval $(l_i, r_i)$ defines a union of 2D axis-aligned rectangles of valid $(L, R)$ pairs. The problem reduces to finding a point $(L, R)$ covered by the maximum number of rectangles, solved via a Sweep Line with a Lazy Segment Tree.
- Common Reductions: Find an open interval $(L, R)$ that intersects the maximum number of given intervals $(l_i, r_i)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc360_f`](../../analysis/AtCoder-abc360_f.md) | F - InterSections | 2563 | Find an open interval $(L, R)$ that intersects the maximum number of given intervals $(l_i, r_i)$.... |
