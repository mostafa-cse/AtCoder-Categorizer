# 2 SAT

**Taxonomy Path**: `Graph Theory` > `Satisfiability` > `2 SAT`

## Description
This topic focuses on 2 sat techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For each bit b in [0, 63], rows and columns impose conditions: (a) all 0, (b) contains 0, (c) all 1, (d) contains 1. Forced rows and columns determine cell values. Conflicts between forced rows and forced columns determine unsatisfiability. Remaining unforced cells are filled to satisfy existence conditions, and final verification validates the 64-bit matrix.
- Common Reductions: Construct an N x N matrix A where row i has bitwise AND/OR equal to U_i and column j has bitwise AND/OR equal to V_j. Because bitwise operations are completely decoupled across bit positions, we solve the problem independently for each bit b in [0, 63] as a binary 2-SAT / constraint satisfaction problem.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc164_f`](../../analysis/AtCoder-abc164_f.md) | I hate Matrix Construction | 2683 | Construct an N x N matrix A where row i has bitwise AND/OR equal to U_i and column j has bitwise AND/OR equal to V_j. Be... |
