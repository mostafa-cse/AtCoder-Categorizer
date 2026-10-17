# Stars and Bars

**Taxonomy Path**: `Basics` > `Basic Counting` > `Stars and Bars`

## Description
This topic focuses on stars and bars techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For any valid tree degree sequence $d_1, \dots, d_N$ with $\sum d_i = 2N - 2$ having $k$ leaves ($d_i = 1$), the maximum possible diameter is achieved by arranging all $N - k$ internal vertices in a simple path, giving maximum diameter $N - k + 1$. Summing $(N - k + 1)$ across all valid degree sequences simplifies algebraically to $(N+1) \binom{2N-3}{N-1} - N \binom{2N-4}{N-2}$.
- Common Reductions: Compute the sum of maximum possible tree diameters over all valid degree sequences of size $N$, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc290_f`](../../analysis/AtCoder-abc290_f.md) | F. Maximum Diameter | 2300 | Compute the sum of maximum possible tree diameters over all valid degree sequences of size $N$, modulo 998244353.... |
