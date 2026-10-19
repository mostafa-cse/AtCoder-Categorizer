# Mobius Function and Mobius Inversion

**Taxonomy Path**: `Number Theory` > `Multiplicative Functions` > `Mobius Function and Mobius Inversion`

## Description
This topic focuses on mobius function and mobius inversion techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Since K <= 10^9, K has at most 10 distinct prime factors and at most 1344 divisors. For each divisor g | K, M = K/g has a subset of K's prime factors. Summing over square-free divisors d | M gives S(L, M) = sum_{d | M} mu(d) * d * (floor(L/d) * (floor(L/d) + 1) / 2). Total operations across all divisors <= 3^{omega(K)} <= 59049.
- Common Reductions: sum_{i=1}^N lcm(i, K) = K * sum_{g | K} sum_{j=1, gcd(j, K/g)=1}^{floor(N/g)} j. For each divisor g of K, the inner coprime sum S(L, M) with M = K/g and L = floor(N/g) is computed in O(2^{omega(M)}) via Mobius inversion / Inclusion-Exclusion over distinct prime factors of M.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc020_d`](../../analysis/AtCoder-abc020_d.md) | LCM Rush | 2695 | sum_{i=1}^N lcm(i, K) = K * sum_{g | K} sum_{j=1, gcd(j, K/g)=1}^{floor(N/g)} j. For each divisor g of K, the inner copr... |
