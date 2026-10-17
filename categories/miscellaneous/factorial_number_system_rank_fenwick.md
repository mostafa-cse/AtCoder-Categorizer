# Factorial Number System

**Taxonomy Path**: `Miscellaneous` > `General` > `Factorial Number System`

## Description
This topic focuses on factorial number system techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because $N!$ is astronomical, we represent the rank in the factorial number system (factoradic). At each step with $m$ remaining unchosen elements, the block size of permutations for the current position is $(m-1)!$. The fraction of remaining permutations we seek is maintained as $\frac{rem}{K}$ where $rem < K$. Multiplying by $m$ gives $\frac{rem \times m}{K}$. Its quotient $q = \lfloor \frac{rem \times m}{K} \rfloor$ determines the 0-based choice index among currently available numbers, and the new remainder is $r = (rem \times m) \bmod K$. If $r = 0$, this step lands exactly at the end of block $q-1$, so the current digit is $q-1$ and all subsequent remaining digits take their maximal values $(m-2, m-3, \dots, 0)$. Available numbers are retrieved and removed using a Fenwick Tree with binary lifting in $O(\log N)$.
- Common Reductions: We are given integers $N$ ($1 \le N \le 10^5$) and $K$ ($1 \le K \le N$). All $N!$ permutations of $(1, 2, \dots, N)$ are arranged in lexicographical order. We must find the $1$-based $\frac{N!}{K}$-th permutation.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc047_c`](../../analysis/AtCoder-arc047_c.md) | C. N!÷K番目の単語 | 2262 | We are given integers $N$ ($1 \le N \le 10^5$) and $K$ ($1 \le K \le N$). All $N!$ permutations of $(1, 2, \dots, N)$ ar... |
