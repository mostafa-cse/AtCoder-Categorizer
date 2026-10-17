# Prefix Sum Queries of Binomial Coefficients

**Taxonomy Path**: `Combinatorics` > `Factorials and Binomial Coefficients (nCr)` > `Prefix Sum Queries of Binomial Coefficients`

## Description
This topic focuses on prefix sum queries of binomial coefficients techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Level $k$ or smaller L-shapes always occupy a square subgrid $I_k \times J_k$ of size $k \times k$, where $[1, N] = I_N \supsetneq \dots \supsetneq I_1$ and $[1, N] = J_N \supsetneq \dots \supsetneq J_1$ are shrinking intervals. Cell $(a, b)$ belongs to level $\le k$ iff $a \in I_k$ and $b \in J_k$. The row and column choices are completely independent! For a 1D sequence of intervals, starting at $[1, N]$ and shrinking by 1 at each step to $[1+x, k+x]$ after $m = N - k$ steps has $\binom{m}{x}$ paths. The condition $a \in [1+x, k+x]$ gives $x \in [\max(0, a-k), \min(N-k, a-1)]$. Hence $F(a, k) = 2^{k-1} \sum_{x} \binom{N-k}{x}$. As $m = N-k$ increments, $\sum \binom{m+1}{x}$ updates in $O(1)$ from $\sum \binom{m}{x}$. The exact level $k$ answer is $F(a, k) F(b, k) - F(a, k-1) F(b, k-1)$.
- Common Reductions: Partition an $N \times N$ grid ($N \le 10^7$) into $N$ L-shapes, one of each level $1, \dots, N$. For $Q \le 200,000$ queries $k_i$, count the partitions where a given cell $(a, b)$ belongs to the level $k_i$ L-shape, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc190_b`](../../analysis/AtCoder-arc190_b.md) | B. L Partition | 2273 | Partition an $N \times N$ grid ($N \le 10^7$) into $N$ L-shapes, one of each level $1, \dots, N$. For $Q \le 200,000$ qu... |
