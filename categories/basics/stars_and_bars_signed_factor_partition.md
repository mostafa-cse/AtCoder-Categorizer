# Stars and Bars

**Taxonomy Path**: `Basics` > `Basic Counting` > `Stars and Bars`

## Description
This topic focuses on stars and bars techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Decompose the problem into magnitudes and signs independently:
1. Magnitudes: Factorize $|N| = \prod_{i=1}^k p_i^{e_i}$. Each prime factor $p_i$ has its exponent $e_i$ partitioned among $M$ factors ($e_{i, 1} + \dots + e_{i, M} = e_i$). By stars and bars, the number of ways is $\binom{e_i + M - 1}{M - 1}$.
2. Signs: Exactly $M$ factors each have a sign $\in \{+1, -1\}$. If $N > 0$, an even number of factors must be negative; if $N < 0$, an odd number of factors must be negative. In either case, the number of valid sign assignments is precisely $\sum \binom{M}{s} = 2^{M - 1}$.
The total answer is $2^{M - 1} \times \prod_{i=1}^k \binom{e_i + M - 1}{M - 1} \pmod{10^9 + 7}$.
- Common Reductions: Given integers $N$ ($1 \le |N| \le 10^9$) and $M$ ($1 \le M \le 10^5$). Count the number of ways to express $N$ as the product of $M$ integers: $N = a_1 \times a_2 \times \dots \times a_M$, with $a_i \in \mathbb{Z}$. Output the result modulo $10^9 + 7$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc004_4`](../../analysis/AtCoder-arc004_4.md) | D. 表現の自由 ( Freedom of expression ) | 2267 | Given integers $N$ ($1 \le |N| \le 10^9$) and $M$ ($1 \le M \le 10^5$). Count the number of ways to express $N$ as the p... |
