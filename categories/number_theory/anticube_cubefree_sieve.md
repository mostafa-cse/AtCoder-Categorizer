# Sieve, Prime Factorization and Divisors

**Taxonomy Path**: `Number Theory` > `Primes and Divisors` > `Sieve, Prime Factorization and Divisors`

## Description
This topic focuses on sieve, prime factorization and divisors techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Remove all cubic prime factors so each s_i is cubefree modulo 3: x = prod p_j^{e_j} (e_j in {1, 2}). The unique dual partner of x is x* = prod p_j^{3 - e_j}. For each pair {x, x*}, at most one group can be chosen, so we greedily pick max(cnt(x), cnt(x*)). If x = 1, we can pick at most 1 element.
- Common Reductions: Given N integers s_i <= 10^{10}, find the maximum size of a subset such that no two elements multiply to a perfect cube.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc003_d`](../../analysis/AtCoder-agc003_d.md) | D. Anticube | 2608 | Given N integers s_i <= 10^{10}, find the maximum size of a subset such that no two elements multiply to a perfect cube.... |
