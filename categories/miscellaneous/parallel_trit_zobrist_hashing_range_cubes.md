# Randomized Algorithms

**Taxonomy Path**: `Miscellaneous` > `Randomized` > `Randomized Algorithms`

## Description
This topic focuses on randomized algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A range product is a cube if and only if the sum of exponents of each prime factor is a multiple of 3. We can map each prime $p$ to a random trit vector in $(\mathbb{Z}_3)^{128}$ represented by two 64-bit masks $(h, l)$. Because addition in $\mathbb{Z}_3$ satisfies $3v = 0$, the prefix sum vector at $R$ equals the prefix sum vector at $L-1$ if and only if all prime exponents in $[L, R]$ are $0 \pmod 3$. Parallel bitwise trit addition enables $O(1)$ query time and $O(N \log \max A)$ precomputation.
- Common Reductions: Given array $A$ of $N$ integers ($A_i \le 10^6$), answer $Q$ queries: is $\prod_{i=L}^R A_i$ a cubic number (perfect cube)?

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc238_g`](../../analysis/AtCoder-abc238_g.md) | G. Cubic? | 2254 | Given array $A$ of $N$ integers ($A_i \le 10^6$), answer $Q$ queries: is $\prod_{i=L}^R A_i$ a cubic number (perfect cub... |
