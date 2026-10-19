# Lagrange Interpolation

**Taxonomy Path**: `Math` > `Polynomial` > `Lagrange Interpolation`

## Description
This topic focuses on lagrange interpolation techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Taking prefix sums of a polynomial sequence increases the polynomial degree by 1. Since A^(0)_i = i^K has degree K, the M-th cumulative sum sequence A^(M)_i is a polynomial in i of degree D = K + M. For any polynomial of degree D, its values at any point N can be recovered from its evaluations at D + 1 points using Lagrange interpolation. We can compute A^(0)_i for i = 0..D in O(D) time using a linear sieve for i^K, perform M prefix sum passes in O(M * D) time, and evaluate at N using O(D) Lagrange interpolation.
- Common Reductions: Given N, M, K, define sequence A^(0)_i = i^K for 0 <= i <= N. For j >= 1, A^(j)_i = sum_{p=0}^i A^(j-1)_p. Compute A^(M)_N mod (10^9 + 7) for N <= 10^18, M <= 30, K <= 2 * 10^6.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc208_f`](../../analysis/AtCoder-abc208_f.md) | F - Cumulative Sum | 2772 | Given N, M, K, define sequence A^(0)_i = i^K for 0 <= i <= N. For j >= 1, A^(j)_i = sum_{p=0}^i A^(j-1)_p. Compute A^(M)... |
