# Mobius Function and Mobius Inversion

**Taxonomy Path**: `Number Theory` > `Multiplicative Functions` > `Mobius Function and Mobius Inversion`

## Description
This topic focuses on mobius function and mobius inversion techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Expressing $\frac{1}{\gcd(x, y)} = \sum_{d \mid \gcd(x, y)} c(d)$ via Dirichlet inversion yields $c(d) = d^{-1} \prod_{p \mid d} (1 - p)$, completely decoupling the pair summation into independent multiple sums.
- Common Reductions: Given array $A$ of length $N$, compute $\sum_{1 \le i < j \le N} \text{lcm}(A_i, A_j) \pmod{998244353}$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc038_c`](../../analysis/AtCoder-agc038_c.md) | C. LCMs | 2327 | Given array $A$ of length $N$, compute $\sum_{1 \le i < j \le N} \text{lcm}(A_i, A_j) \pmod{998244353}$.... |
