# Manhattan <> Chebyshev

**Taxonomy Path**: `Miscellaneous` > `Techniques` > `Manhattan <> Chebyshev`

## Description
This topic focuses on manhattan <> chebyshev techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any equilateral triangle in Chebyshev metric cannot have all three pairwise distances along the same axis. Therefore, at least two points share the same $u$ or same $v$. Triangles with a flat horizontal side are queried via 2D prefix sums over vertical ranges; triangles with a flat vertical side are queried similarly. Triangles forming three corners of an axis-aligned square (L-shapes) are counted twice and subtracted.
- Common Reductions: Count triples of points with equal pairwise Manhattan distances. Manhattan distance rotates 45 degrees into Chebyshev distance $\max(|u_i - u_j|, |v_i - v_j|)$ with $u = r + c, v = r - c + W$. In Chebyshev distance, pairwise distances $D$ must be even, and any equilateral triangle consists of two points lying along an axis-aligned boundary of size $D$ and a third point on the parallel opposite boundary $[v_1, v_2]$ or $[u_1, u_2]$. Range queries count candidate points, while subtracting L-shaped 3-corner overlaps avoids overcounting.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-tenka1_2018_e`](../../analysis/AtCoder-tenka1_2018_e.md) | E. Equilateral | 2459 | Count triples of points with equal pairwise Manhattan distances. Manhattan distance rotates 45 degrees into Chebyshev di... |
