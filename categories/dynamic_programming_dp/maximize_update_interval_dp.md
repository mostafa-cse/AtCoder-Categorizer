# Interval DP / Range DP / Matrix Chain Multiplication (MCM)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Classic DP` > `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`

## Description
This topic focuses on interval dp / range dp / matrix chain multiplication (mcm) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Consider the last square $k \in [l, r]$ to be newly painted. The operation covering $k$ must be strictly contained inside $[l, r]$. All other operations painting squares in $[l, k-1]$ or $[k+1, r]$ cannot cover $k$, separating the problem into completely independent subintervals $[l, k-1]$ and $[k+1, r]$. An interval covering $k$ inside $[l, r]$ exists iff $\max \{ L_i \mid L_i \le k \le R_i \le r \} \ge l$.
- Common Reductions: Maximize the number of operations that paint at least one previously white square black, given $M$ candidate intervals $[L_i, R_i]$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc168_d`](../../analysis/AtCoder-arc168_d.md) | D. Maximize Update | 2440 | Maximize the number of operations that paint at least one previously white square black, given $M$ candidate intervals $... |
