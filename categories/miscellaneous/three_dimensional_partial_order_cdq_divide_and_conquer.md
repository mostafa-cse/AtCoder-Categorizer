# CDQ Divide and Conquer

**Taxonomy Path**: `Miscellaneous` > `Techniques` > `CDQ Divide and Conquer`

## Description
This topic focuses on cdq divide and conquer techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The reachability condition |X_j - X_i| + Y_j - Y_i <= T_j - T_i with Y_j >= Y_i linearizes under coordinate transformation a = T - X - Y >= 0, b = T + X - Y >= 0, c = Y >= 0. Reachability becomes a 3D partial order: a_i <= a_j, b_i <= b_j, c_i <= c_j. This is solved by CDQ divide-and-conquer on 3D weighted DAG / LIS DP in O(N log^2 N) time.
- Common Reductions: Takahashi starts at (0, 0) at time 0. He can move at speed <= 1 in x and speed <= 1 in positive y (y cannot decrease). N Snuke appear at times T_i, coordinates (X_i, Y_i), with sizes A_i. Maximize the total size of captured Snuke.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc266_h`](../../analysis/AtCoder-abc266_h.md) | Ex - Snuke Panic (2D) | 2865 | Takahashi starts at (0, 0) at time 0. He can move at speed <= 1 in x and speed <= 1 in positive y (y cannot decrease). N... |
