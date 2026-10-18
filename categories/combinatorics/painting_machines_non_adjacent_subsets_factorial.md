# Large Factorials and Binomial Coefficients

**Taxonomy Path**: `Combinatorics` > `Factorials and Binomial Coefficients (nCr)` > `Large Factorials and Binomial Coefficients`

## Description
This topic focuses on large factorials and binomial coefficients techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Operating machines in subset $S$ covers all $N$ squares iff machines 1 and $N-1$ are selected and no two unchosen machines in $\{2, \dots, N-2\}$ are adjacent. For $|S| = k$, the number of valid subsets is $\binom{k - 1}{N - 1 - k}$. The number of permutations where all squares are covered within the first $k$ steps is $F(k) = \binom{k - 1}{N - 1 - k} k! (N - 1 - k)!$.
- Common Reductions: Evaluate the sum of operation counts across all $(N-1)!$ permutations of painting machines until all $N$ squares are painted black.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc023_c`](../../analysis/AtCoder-agc023_c.md) | C. Painting Machines | 2568 | Evaluate the sum of operation counts across all $(N-1)!$ permutations of painting machines until all $N$ squares are pai... |
