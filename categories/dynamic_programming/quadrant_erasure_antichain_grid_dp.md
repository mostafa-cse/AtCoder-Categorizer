# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any non-empty remaining set must form an antichain (strictly decreasing sequence of Y coordinates when ordered by X). Furthermore, a set is reachable if and only if it is maximal among antichains: no omitted ball between adjacent elements i and j could have survived without being erased by one of the selected balls. By adding sentinel boundary points at (0, N+1) and (N+1, 0), transition from i to j (with i < j, P_i > P_j) is valid if and only if no point k in between has empty rectangular regions (i, k, P_j, P_k) and (k+1, j, P_k+1, P_i). This yields an O(N^3) DP over the DAG of valid transitions.
- Common Reductions: Given N balls on a 2D grid with permutation coordinates (X_i, Y_i), any chosen ball k erases all balls in its bottom-left and top-right quadrants. Find the number of distinct subsets of balls that can remain after any sequence of operations modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc184_d`](../../analysis/AtCoder-arc184_d.md) | D - Erase Balls 2D | 2804 | Given N balls on a 2D grid with permutation coordinates (X_i, Y_i), any chosen ball k erases all balls in its bottom-lef... |
