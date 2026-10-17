# Points, Vectors, Transformations, Dot Products, Cross Products, Precision Issues and Polar Sort(2D)

**Taxonomy Path**: `Geometry` > `Geometry 2D` > `Points, Vectors, Transformations, Dot Products, Cross Products, Precision Issues and Polar Sort(2D)`

## Description
This topic focuses on points, vectors, transformations, dot products, cross products, precision issues and polar sort(2d) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Total triangles is C(N, 3). Each triangle has at most one right angle and at most one obtuse angle. Thus, counting right triangles and obtuse triangles reduces to counting pairs of vectors from a common pivot vertex that form an angle of exactly 90 degrees or > 90 degrees. For each point P_i, polar sorting the angles of all other N - 1 points allows finding right and obtuse angles in O(N log N) using two pointers.
- Common Reductions: Count the number of acute, right, and obtuse triangles formed by N <= 2000 points in the plane with no three points collinear.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc033_d`](../../analysis/AtCoder-abc033_d.md) | 三角形の分類 | 2248 | Count the number of acute, right, and obtuse triangles formed by N <= 2000 points in the plane with no three points coll... |
