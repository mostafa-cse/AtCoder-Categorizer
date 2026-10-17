# Multiplicative Order and Carmichael's Lambda Function

**Taxonomy Path**: `Number Theory` > `Modular Arithmetic` > `Multiplicative Order and Carmichael's Lambda Function`

## Description
This topic focuses on multiplicative order and carmichael's lambda function techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In the binomial expansion (1 + N)^n = 1 + nN + C(n, 2) N^2 + ..., every term for k >= 2 contains N^k and is divisible by N^2. Thus (N+1)^n = 1 + nN mod N^2 for all n, so the smallest positive integer with (N+1)^n = 1 mod N^2 is n = N. Since N <= 10^9, N^2 <= 10^{18} fits in a 64-bit integer.
- Common Reductions: Find (A, M) with A, M <= 10^18 such that ord_M(A) = N. Setting (A, M) = (N + 1, N^2) guarantees that (N+1)^n = 1 + nN mod N^2 by the Binomial Theorem, so (N+1)^n = 1 mod N^2 iff N divides n, making the order exactly N for all N >= 2. For N = 1, (2, 1) works.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc191_c`](../../analysis/AtCoder-arc191_c.md) | C. A^n - 1 | 2198 | Find (A, M) with A, M <= 10^18 such that ord_M(A) = N. Setting (A, M) = (N + 1, N^2) guarantees that (N+1)^n = 1 + nN mo... |
