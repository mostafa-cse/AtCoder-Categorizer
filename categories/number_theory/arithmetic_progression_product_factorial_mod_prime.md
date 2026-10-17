# Wilson's Theorem

**Taxonomy Path**: `Number Theory` > `Primes and Divisors` > `Wilson's Theorem`

## Description
This topic focuses on wilson's theorem techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Let $P = 1000003$ (prime). If $d = 0$, the answer is $x^n \pmod P$. If $n \ge P$, at least one term is $0 \pmod P$, so the product is 0. If $n < P$ and $d \ne 0$, factor out $d$: $\prod (x + i d) = d^n \prod_{i=0}^{n-1} (k + i) \pmod P$ where $k = x d^{-1} \pmod P$. If $k + n - 1 \ge P$, the product wraps through $0 \pmod P$ and is 0; otherwise it is $d^n \frac{(k+n-1)!}{(k-1)!} \pmod P$, evaluated in $O(1)$ after $O(P)$ precomputation.
- Common Reductions: Answer $Q$ queries: compute the product of an arithmetic progression $\prod_{i=0}^{n-1} (x + i d) \pmod{1000003}$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-m_solutions2019_e`](../../analysis/AtCoder-m_solutions2019_e.md) | E. Product of Arithmetic Progression | 2261 | Answer $Q$ queries: compute the product of an arithmetic progression $\prod_{i=0}^{n-1} (x + i d) \pmod{1000003}$.... |
