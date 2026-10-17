# Segmented Sieve

**Taxonomy Path**: `Number Theory` > `Primes and Divisors` > `Segmented Sieve`

## Description
This topic focuses on segmented sieve techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: C(N, K) = prod_{i=0}^{K-1} (N - i) / K!. Any prime p <= 10^6 divides terms in the interval and in K!, counted via Legendre formula. Any remaining factor > 1 in val[i] after dividing out all primes <= 10^6 must itself be a prime > 10^6, which appears at most once across the interval [N - K + 1, N] since interval length is K <= 10^6.
- Common Reductions: Prime factorization of C(N, K) using segmented sieve over numerator interval [N - K + 1, N] and small prime trial division.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc227_g`](../../analysis/AtCoder-abc227_g.md) | Divisors of Binomial Coefficient | 2207 | Prime factorization of C(N, K) using segmented sieve over numerator interval [N - K + 1, N] and small prime trial divisi... |
