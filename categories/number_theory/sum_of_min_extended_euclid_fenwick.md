# Extended Euclid

**Taxonomy Path**: `Number Theory` > `Euclidean Algorithm` > `Extended Euclid`

## Description
This topic focuses on extended euclid techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By the Chinese Remainder Theorem and Bezout's identity, the pair $(k \bmod N, k \bmod M)$ visits each pair $(i, j)$ where $i \equiv j \pmod{g}$ exactly $g$ times, where $g = \gcd(N, M)$. This decomposes the problem into $g$ independent subproblems of sizes $N/g$ and $M/g$. Within each subproblem, elements of $B$ can be permuted along arithmetic progressions modulo $M/g$, converting the sum of minima into circular range queries evaluated using a Fenwick tree.
- Common Reductions: Compute $\sum_{k=0}^{NM-1} \min(A_{k \bmod N}, B_{k \bmod M})$ efficiently.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc438_g`](../../analysis/AtCoder-abc438_g.md) | G - Sum of Min | 2455 | Compute $\sum_{k=0}^{NM-1} \min(A_{k \bmod N}, B_{k \bmod M})$ efficiently.... |
