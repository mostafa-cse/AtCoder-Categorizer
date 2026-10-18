# Sweep Line Algorithm and Radial Sweep

**Taxonomy Path**: `Geometry` > `Sweep Line` > `Sweep Line Algorithm and Radial Sweep`

## Description
This topic focuses on sweep line algorithm and radial sweep techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In any rectilinear polygon, when oriented counter-clockwise, vertical edges going downward enter the polygon interior (adding $+1$ to the $y$-interval), while vertical edges going upward exit the interior (adding $-1$). Point location for $(X + 0.5, Y + 0.5)$ reduces to a 1D point query on the accumulated interval status at $x \le X$ via sweep-line.
- Common Reductions: Answer point location queries in $N$ rectilinear polygons. CCW orientation determines whether vertical edges enter (+1) or exit (-1) the interior, evaluated by sweeping $x$ with a difference-array Fenwick tree in $O((M + Q) \log (\max Y))$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc211_f`](../../analysis/AtCoder-abc211_f.md) | F. Rectilinear Polygons | 2350 | Answer point location queries in $N$ rectilinear polygons. CCW orientation determines whether vertical edges enter (+1) ... |
