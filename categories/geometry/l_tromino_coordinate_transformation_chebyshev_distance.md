# Points, Vectors, Transformations, Dot Products, Cross Products, Precision Issues and Polar Sort(2D)

**Taxonomy Path**: `Geometry` > `Geometry 2D` > `Points, Vectors, Transformations, Dot Products, Cross Products, Precision Issues and Polar Sort(2D)`

## Description
This topic focuses on points, vectors, transformations, dot products, cross products, precision issues and polar sort(2d) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any L-tromino is uniquely characterized by the coordinate sum (X, Y) = (ax + bx + cx, ay + by + cy). Applying coordinate transformation x' = f(X) and y' = f(Y) maps the state space onto a grid where one stone move corresponds to Chebyshev distance with a parity correction: dist = max(|x'|, |y'|) + [x' == y'].
- Common Reductions: Summing coordinates uniquely identifies L-tromino configurations. A geometric transformation reduces moves to Chebyshev metric distance with parity adjustment on the diagonal, answering each testcase in O(1) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc109_d`](../../analysis/AtCoder-arc109_d.md) | D. L | 2394 | Summing coordinates uniquely identifies L-tromino configurations. A geometric transformation reduces moves to Chebyshev ... |
