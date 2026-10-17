# Multiplicative Order and Carmichael's Lambda Function

**Taxonomy Path**: `Number Theory` > `Modular Arithmetic` > `Multiplicative Order and Carmichael's Lambda Function`

## Description
This topic focuses on multiplicative order and carmichael's lambda function techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The n-th term is 2(10^n - 1)/9. Thus 2(10^n - 1)/9 = 0 (mod K) <=> 2(10^n - 1) = 0 (mod 9K). Let M = 9K / gcd(2, 9K). The equation becomes 10^n = 1 (mod M). A solution exists iff gcd(10, M) == 1. When gcd(10, M) == 1, the smallest n is the multiplicative order of 10 modulo M, which must divide Euler's totient phi(M). We can factorize phi(M) and test its divisors.
- Common Reductions: Find the smallest positive integer n such that the n-digit repunit 22...2 is divisible by K, or determine that no such n exists.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc222_g`](../../analysis/AtCoder-abc222_g.md) | 222 | 2242 | Find the smallest positive integer n such that the n-digit repunit 22...2 is divisible by K, or determine that no such n... |
