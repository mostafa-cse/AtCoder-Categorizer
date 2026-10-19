# 2D Prefix Sum

**Taxonomy Path**: `Basics` > `2D Prefix Sum` > `2D Prefix Sum`

## Description
This topic focuses on 2d prefix sum techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any point can be moved to any lattice position with the same (x mod D, y mod D). For an enclosing square of side length aD + b with offset (X, Y), each residue cell has capacity (a+1)^2, a(a+1), or a^2 forming 4 rectangular quadrants. Feasibility requires: all cells with count > a(a+1) lie in a (b+1) x (b+1) window, and no cell with count > a^2 lies in the forbidden (D - 1 - b) x (D - 1 - b) window. Using 2D prefix sums on a periodic 2D x 2D grid, each offset (X, Y) is tested in O(1) time.
- Common Reductions: Given N points in Z^2 and integer D, 90-degree rotations of D x D squares preserve coordinates modulo D. Find the minimum side length of an axis-aligned square that can enclose all points after arbitrary operations.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-dwacon5th_prelims_d`](../../analysis/AtCoder-dwacon5th_prelims_d.md) | D - Square Rotation | 2875 | Given N points in Z^2 and integer D, 90-degree rotations of D x D squares preserve coordinates modulo D. Find the minimu... |
