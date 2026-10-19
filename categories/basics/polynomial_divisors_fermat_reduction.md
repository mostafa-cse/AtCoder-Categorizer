# Fermat's Little Theorem and Modular Inverse

**Taxonomy Path**: `Basics` > `Basic Modular Arithmetic` > `Fermat's Little Theorem and Modular Inverse`

## Description
This topic focuses on fermat's little theorem and modular inverse techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By Fermat's Little Theorem, x^k = x^{1 + (k - 1) mod (p - 1)} (mod p) for all x not divisible by p (and for x = 0, x^k = 0 for all k >= 1). Thus, modulo p, any polynomial reduces to an equivalent polynomial of degree at most p - 1. A polynomial of degree < p evaluates to 0 mod p for all integers x if and only if all of its reduced coefficients are 0 mod p! For primes p <= N, we can directly compute the reduced coefficients modulo p and verify if all are divisible by p. For primes p > N, no reduction of degree can occur, so f(x) = 0 mod p for all x requires all original coefficients a_i to be divisible by p, meaning p must divide gcd(a_0, a_1, ..., a_N).
- Common Reductions: Given an integer polynomial f(x) = a_N x^N + ... + a_1 x + a_0, find all prime numbers p such that p divides f(x) for all integers x.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-tenka1_2019_e`](../../analysis/AtCoder-tenka1_2019_e.md) | E - Polynomial Divisors | 2742 | Given an integer polynomial f(x) = a_N x^N + ... + a_1 x + a_0, find all prime numbers p such that p divides f(x) for al... |
