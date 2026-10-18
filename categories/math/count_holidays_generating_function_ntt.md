# Number Theoretic Transform (NTT)

**Taxonomy Path**: `Math` > `Convolution` > `Number Theoretic Transform (NTT)`

## Description
This topic focuses on number theoretic transform (ntt) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Holidays cannot cross forced workdays 'x', so $S$ splits into independent dot blocks of lengths $L_1, \dots, L_m$. Let $F(S, k)$ be schedules with longest holiday run $\le k$. Then $F(S, k) = \prod_j f(L_j, k)$. By generating functions or inclusion-exclusion, $f(n, k) = [x^n] \frac{1 - x^{k+1}}{1 - 2x + x^{k+2}} = \sum_{m=0}^{\lfloor (n+1)/(k+2) \rfloor} (-1)^m g(n, k, m)$, which evaluates in $O(n / (k+2))$ time. Summing over all $k$ yields total complexity $O(N \log N)$.
- Common Reductions: Count work schedules satisfying work-day constraints where the longest run of consecutive holidays is exactly $k$, for every $1 \le k \le N$ modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc456_g`](../../analysis/AtCoder-abc456_g.md) | G - Count Holidays | 2488 | Count work schedules satisfying work-day constraints where the longest run of consecutive holidays is exactly $k$, for e... |
