# Floor Sum and Mod Sum of Arithmetic Progression

**Taxonomy Path**: `Number Theory` > `Floor Sum` > `Floor Sum and Mod Sum of Arithmetic Progression`

## Description
This topic focuses on floor sum and mod sum of arithmetic progression techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For each x >= 1, the upper bound on y is the lower envelope of the lines y = (C_i - A_i x) / B_i. The feasible region is bounded by this upper convex envelope consisting of at most N linear segments. On each segment [x_k, x_{k+1}] defined by a line A x + B y <= C, the number of integer points with 1 <= y <= floor((C - A x) / B) can be computed in O(log(A + B)) time using the standard floor_sum algorithm.
- Common Reductions: Given T test cases, each with N linear inequalities A_i x + B_i y <= C_i with x, y >= 1, count the number of integer pairs (x, y) satisfying all inequalities simultaneously.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc372_g`](../../analysis/AtCoder-abc372_g.md) | G. Ax + By < C | 2925 | Given T test cases, each with N linear inequalities A_i x + B_i y <= C_i with x, y >= 1, count the number of integer pai... |
