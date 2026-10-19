# Sieve, Prime Factorization and Divisors

**Taxonomy Path**: `Number Theory` > `Primes and Divisors` > `Sieve, Prime Factorization and Divisors`

## Description
This topic focuses on sieve, prime factorization and divisors techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Let shared digits be d_k ... d_0. The value difference is sum_{i=0}^k d_i (b^i - a^i) = X.
- For k = 2 (2 digits): d_1 (b - a) = X. For each divisor d of X with d_1 = d, count a such that d < a <= N - X/d.
- For k = 3 (3 digits): (b - a)(d_2(a+b) + d_1) = X. Divisors of X yield pairs (a, b).
- For k >= 4: since b >= 3, b^3 <= X implies b <= X^{1/3} <= 10^6. We can directly iterate over (a, b) and greedily verify digits.
- Common Reductions: Given N and X, count pairs of bases (a, b) with 2 <= a < b <= N such that some integer has identical digits in base a and base b, and the difference in values is X, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc322_g`](../../analysis/AtCoder-abc322_g.md) | G. Two Kinds of Base | 2876 | Given N and X, count pairs of bases (a, b) with 2 <= a < b <= N such that some integer has identical digits in base a an... |
