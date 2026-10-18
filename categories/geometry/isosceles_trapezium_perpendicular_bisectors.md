# Polygons(2D)

**Taxonomy Path**: `Geometry` > `Geometry 2D` > `Polygons(2D)`

## Description
This topic focuses on polygons(2d) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Pairs sharing the same midpoint along the line are collinear and cannot form a valid quadrilateral. For each distinct parallel position on the bisector line, we keep only the pair with maximum weight, and then test the top pairs with disjoint vertex sets.
- Common Reductions: Choose 4 points out of $N \le 1000$ to form an isosceles trapezoid of maximum total weight. Four points form an isosceles trapezoid iff they can be paired into two parallel segments whose perpendicular bisectors are identical lines. Grouping all $\binom{N}{2}$ pairs by their canonical perpendicular bisector line equation $(A, B, C)$ allows finding the two heaviest disjoint pairs along each symmetry line.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc220_g`](../../analysis/AtCoder-abc220_g.md) | G. Isosceles Trapezium | 2439 | Choose 4 points out of $N \le 1000$ to form an isosceles trapezoid of maximum total weight. Four points form an isoscele... |
