# Randomized Algorithms

**Taxonomy Path**: `Miscellaneous` > `Randomized` > `Randomized Algorithms`

## Description
This topic focuses on randomized algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Both sides of the equation are homogeneous polynomials: LHS has degree 1 + n + 2n = 3n + 1, while RHS has degree 3n. If we choose distinct random non-zero (x_0, y_0, z_0) and scale them by factor k, LHS becomes k^{3n+1} LHS_0 and RHS becomes k^{3n} RHS_0. Equating LHS and RHS gives k = RHS_0 / LHS_0 mod p. As long as LHS_0 != 0 and RHS_0 != 0, this yields a valid scaling factor k in O(log p) time.
- Common Reductions: Given n and prime p, find three distinct integers x, y, z in [1, p-1] satisfying (x+y+z)(x^n+y^n+z^n)(x^{2n}+y^{2n}+z^{2n}) = x^{3n}+y^{3n}+z^{3n} modulo p.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc158_d`](../../analysis/AtCoder-arc158_d.md) | D. Equation | 2893 | Given n and prime p, find three distinct integers x, y, z in [1, p-1] satisfying (x+y+z)(x^n+y^n+z^n)(x^{2n}+y^{2n}+z^{2... |
