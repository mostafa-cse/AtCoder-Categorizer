# Sieve, Prime Factorization and Divisors

**Taxonomy Path**: `Number Theory` > `Primes and Divisors` > `Sieve, Prime Factorization and Divisors`

## Description
This topic focuses on sieve, prime factorization and divisors techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Only square-free integers $g, h > 1$ with $\mu \ne 0$ need to be considered. For a fixed square-free $g > 1$, consider all indices $i$ that are multiples of $g$ ($i = c \cdot g$). For each such index, factorize $P_i$ into its square-free divisors $h > 1$ and count occurrences in a frequency array. The sum of divisor counts over all multiples of $g$ across all $g$ is $\sum_{g} \sum_{c=1}^{N/g} d(P_{cg}) \approx O(N \log^2 N)$, which requires $\le 7 \times 10^6$ operations.
- Common Reductions: Count pairs $(i, j)$ with $1 \le i \le j \le N$ such that $\gcd(i, j) > 1$ and $\gcd(P_i, P_j) > 1$. Condition $[\gcd > 1] = 1 - [\gcd = 1] = - \sum_{g > 1} \mu(g) [g \mid \gcd]$. Applying Mobius inversion to both indices and values expresses the condition as double Mobius inversion: $\sum_{g > 1, h > 1} \mu(g) \mu(h) \binom{cnt(g, h) + 1}{2}$, where $cnt(g, h)$ is the number of indices $i$ such that $g \mid i$ and $h \mid P_i$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc230_g`](../../analysis/AtCoder-abc230_g.md) | G. GCD Permutation | 2516 | Count pairs $(i, j)$ with $1 \le i \le j \le N$ such that $\gcd(i, j) > 1$ and $\gcd(P_i, P_j) > 1$. Condition $[\gcd > ... |
