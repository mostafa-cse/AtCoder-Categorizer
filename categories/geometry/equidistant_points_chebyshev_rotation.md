# Points, Vectors, Transformations, Dot Products, Cross Products, Precision Issues and Polar Sort(2D)

**Taxonomy Path**: `Geometry` > `Geometry 2D` > `Points, Vectors, Transformations, Dot Products, Cross Products, Precision Issues and Polar Sort(2D)`

## Description
This topic focuses on points, vectors, transformations, dot products, cross products, precision issues and polar sort(2d) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Rotating coordinates by 45 degrees via $(u, v) = (x+y, x-y)$ converts Manhattan distance to $\ell_\infty$ Chebyshev distance $\max(|u_1 - u_2|, |v_1 - v_2|)$. A circle of radius $D$ in $\ell_\infty$ is the boundary of an axis-aligned square of side length $2D$. All points must lie on the boundary of $[U - D, U + D] \times [V - D, V + D]$. Thus $2D = \max(u_{\max} - u_{\min}, v_{\max} - v_{\min})$, and the center $(U, V)$ must be one of at most 4 candidates $(u_{\min}+D, u_{\max}-D) \times (v_{\min}+D, v_{\max}-D)$. Testing these 4 candidates in $O(N)$ identifies the valid center point.
- Common Reductions: Find a lattice point $P = (P_x, P_y)$ with $|P_x|, |P_y| \le 10^9$ equidistant in Manhattan metric from all $N$ given points.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc047_b`](../../analysis/AtCoder-arc047_b.md) | B - 同一円周上 | 2455 | Find a lattice point $P = (P_x, P_y)$ with $|P_x|, |P_y| \le 10^9$ equidistant in Manhattan metric from all $N$ given po... |
