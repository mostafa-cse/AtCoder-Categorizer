# Linear Recurrence using Cayley-Hamilton Theorem in O(N^2 log K)

**Taxonomy Path**: `Math` > `Linear Recurrence` > `Linear Recurrence using Cayley-Hamilton Theorem in O(N^2 log K)`

## Description
This topic focuses on linear recurrence using cayley-hamilton theorem in o(n^2 log k) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Every N x N matrix satisfies its characteristic polynomial P(lambda) = det(lambda * I - A) = 0 of degree N. Hence any power A^K reduces modulo P(lambda) to a polynomial R(A) = sum_{j=0}^{N-1} r_j A^j via polynomial binary exponentiation in O(N^2 log K). By linearity of expectation and cycle decompositions over independent uniform variables, summing Tr(A^K) decomposes into evaluating trace sums and characteristic polynomials over fixed walk configurations.
- Common Reductions: Given an N x N matrix A with some known values and some free variables in {0..p-1}, compute the sum of Tr(A^K) over all choices of free variables modulo p, utilizing the Cayley-Hamilton theorem and polynomial reduction.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc190_d`](../../analysis/AtCoder-arc190_d.md) | D - Matrix Pow Sum | 2802 | Given an N x N matrix A with some known values and some free variables in {0..p-1}, compute the sum of Tr(A^K) over all ... |
