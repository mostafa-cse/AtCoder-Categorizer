# Mobius Function and Mobius Inversion

**Taxonomy Path**: `Number Theory` > `Multiplicative Functions` > `Mobius Function and Mobius Inversion`

## Description
This topic focuses on mobius function and mobius inversion techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Repunits $R_n = (10^n - 1)/9$ form a strong divisibility sequence satisfying $\gcd(R_a, R_b) = R_{\gcd(a, b)}$. By multiplicative Möbius inversion, $R_n = \prod_{d | n} f(d)$ where $f(d) = \prod_{c | d} R_c^{\mu(d/c)}$, and $\mathrm{LCM}(R_{A_1}, \dots, R_{A_k}) = \prod_{d \in \bigcup_{i=1}^k \mathrm{divisors}(A_i)} f(d)$.
- Common Reductions: Given an array of indices $A_1, \dots, A_N$, find the least common multiple of repunits $R_{A_1}, \dots, R_{A_k}$ modulo 998244353 for every prefix $k = 1, \dots, N$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc202_c`](../../analysis/AtCoder-arc202_c.md) | C. Repunits | 2274 | Given an array of indices $A_1, \dots, A_N$, find the least common multiple of repunits $R_{A_1}, \dots, R_{A_k}$ modulo... |
