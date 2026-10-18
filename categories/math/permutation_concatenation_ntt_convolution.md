# Number Theoretic Transform (NTT)

**Taxonomy Path**: `Math` > `Convolution` > `Number Theoretic Transform (NTT)`

## Description
This topic focuses on number theoretic transform (ntt) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each number $x \in \{1, \dots, N\}$ has digit length $d(x) = \lfloor \log_{10} x \rfloor + 1$. In a permutation, the contribution of $x$ depends on its value $x$ and the sum of digit lengths of all numbers appearing after $x$. Partition the numbers $1 \dots N$ into at most 6 buckets based on their digit lengths $d \in \{1, 2, 3, 4, 5, 6\}$. For each bucket, the generating function of the exponent $\sum 10^{d(y)}$ factorizes as a product of polynomials $\prod (1 + 10^{d_i} t)$, solved via divide-and-conquer NTT polynomial multiplication.
- Common Reductions: Compute the sum of integers formed by concatenating all $N!$ permutations of $(1, 2, \dots, N)$ modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc390_g`](../../analysis/AtCoder-abc390_g.md) | G - Permutation Concatenation | 2508 | Compute the sum of integers formed by concatenating all $N!$ permutations of $(1, 2, \dots, N)$ modulo 998244353.... |
