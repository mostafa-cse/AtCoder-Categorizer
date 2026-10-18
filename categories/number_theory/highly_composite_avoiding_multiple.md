# Number of Divisors / Sum of Divisors / Sigma Function

**Taxonomy Path**: `Number Theory` > `Multiplicative Functions` > `Number of Divisors / Sum of Divisors / Sigma Function`

## Description
This topic focuses on number of divisors / sum of divisors / sigma function techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A positive integer $x \le N$ is not a multiple of $D$ iff there exists at least one prime factor $p \mid D$ such that $v_p(x) < v_p(D)$. Any integer maximizing the divisor count $d(x)$ has non-increasing prime factor exponents $v_2(x) \ge v_3(x) \ge v_5(x) \ge \dots$, except possibly for the single restricted prime factor $p$.
- Common Reductions: Find an integer $x \le N$ not divisible by $D$ with the maximum number of divisors. Enforcing $v_p(x) < v_p(D)$ for at least one prime factor $p \mid D$ restricts the search to non-increasing exponent sequences with at most one exception, explored via branch-and-bound DFS.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc475_g`](../../analysis/AtCoder-abc475_g.md) | G. Has Many Divisors | 2360 | Find an integer $x \le N$ not divisible by $D$ with the maximum number of divisors. Enforcing $v_p(x) < v_p(D)$ for at l... |
