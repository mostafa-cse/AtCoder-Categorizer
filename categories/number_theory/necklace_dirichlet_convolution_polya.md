# Dirichlet convolution

**Taxonomy Path**: `Number Theory` > `Multiplicative Functions` > `Dirichlet convolution`

## Description
This topic focuses on dirichlet convolution techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Since each jewel has beauty $\ge 2$, the maximum necklace length is $V = \lfloor \log_2 U \rfloor \le 20$. Let $A[n][s]$ be the number of linear jewel sequences of length $n$ with product $s$, which is computed by Dirichlet DP in $O(U \log^2 U)$. By Polya's Enumeration Theorem / Burnside's Lemma, rotational symmetry over length $L$ yields $\frac{1}{L} \sum_{d | L} \varphi(d) A[L/d][x^{1/d}]$. Summing over all $L \le V$ evaluates the count for all $x \le U$ simultaneously.
- Common Reductions: Count the number of non-empty circular necklaces of jewels modulo 998244353 whose beauty product equals $x$ for each $2 \le x \le U$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc428_g`](../../analysis/AtCoder-abc428_g.md) | G - Necklace | 2472 | Count the number of non-empty circular necklaces of jewels modulo 998244353 whose beauty product equals $x$ for each $2 ... |
