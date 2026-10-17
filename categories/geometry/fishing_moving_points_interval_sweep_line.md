# Sweep Line Algorithm and Radial Sweep

**Taxonomy Path**: `Geometry` > `Sweep Line` > `Sweep Line Algorithm and Radial Sweep`

## Description
This topic focuses on sweep line algorithm and radial sweep techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Without loss of generality, at the optimal moment, some fish i lies exactly at the left boundary of the net: x = X_i + t V_i. For a fixed reference fish i, any other fish j is inside the net [x, x + A] iff 0 <= (X_j - X_i) + t(V_j - V_i) <= A, which defines a closed time interval [L_{i,j}, R_{i,j}] cap [0, infty).
- Common Reductions: 1D event sweep line over time intervals of fish containment with respect to reference fish coordinate.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc274_f`](../../analysis/AtCoder-abc274_f.md) | Fishing | 2212 | 1D event sweep line over time intervals of fish containment with respect to reference fish coordinate.... |
