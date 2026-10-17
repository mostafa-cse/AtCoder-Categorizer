# Sieve, Prime Factorization and Divisors

**Taxonomy Path**: `Number Theory` > `Primes and Divisors` > `Sieve, Prime Factorization and Divisors`

## Description
This topic focuses on sieve, prime factorization and divisors techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Operation $x \leftarrow \gcd(x, y)$ can only reduce values, so the final single remaining value cannot exceed $m = \min(A)$. Any integer $d \le m$ is reachable as a final value if and only if the GCD of all array elements that are multiples of $d$ is exactly $d$.
- Common Reductions: Repeatedly replacing $(x, y)$ with $\gcd(x, y)$ or $\min(x, y)$ can achieve any divisor $d \le \min(A)$ if and only if the GCD of all array elements divisible by $d$ is exactly $d$. Evaluated by factorizing all elements in $O(N \sqrt{\max A})$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc191_f`](../../analysis/AtCoder-abc191_f.md) | F. GCD or MIN | 2333 | Repeatedly replacing $(x, y)$ with $\gcd(x, y)$ or $\min(x, y)$ can achieve any divisor $d \le \min(A)$ if and only if t... |
