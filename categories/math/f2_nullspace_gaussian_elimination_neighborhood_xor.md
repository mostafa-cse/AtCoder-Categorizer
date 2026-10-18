# Gaussian Elimination Modulo 2

**Taxonomy Path**: `Math` > `Linear Algebra` > `Gaussian Elimination Modulo 2`

## Description
This topic focuses on gaussian elimination modulo 2 techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The condition XOR_{u in N(v)} X_u = 0 is bitwise independent and equivalent to A x = 0 over F_2. Requiring X_v > 0 for all v means for each vertex v, there must exist a vector in ker(A) with x_v = 1. With N <= 60 and 60 bits available, solving N linear systems over F_2 guarantees each vertex receives at least one 1-bit.
- Common Reductions: Assign non-zero integers X_v in [1, 2^60 - 1] to graph vertices such that for each vertex of degree >= 1, the XOR sum of neighbors is 0. Formulate each bit independently as finding a vector in the nullspace of the adjacency matrix over F_2.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc366_g`](../../analysis/AtCoder-abc366_g.md) | G. XOR Neighbors | 2409 | Assign non-zero integers X_v in [1, 2^60 - 1] to graph vertices such that for each vertex of degree >= 1, the XOR sum of... |
