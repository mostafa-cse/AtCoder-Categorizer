# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By queue multiset rephrasing: two elements a_i, a_j coexist in the active shuffle window with probability p^{f(j)-f(i)} where p = (K-1)/K and f(i) = max(0, i-K+1). If they coexist, their relative order is inverted with probability 1/2; if they never coexist, they maintain their original order.
- Common Reductions: Given permutation P of length N and window size K, shuffle P[i ... i+K-1] uniformly randomly for i = 1 ... N-K+1 in order. Find expected inversion number modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-acl1_e`](../../analysis/AtCoder-acl1_e.md) | E. Shuffle Window | 2605 | Given permutation P of length N and window size K, shuffle P[i ... i+K-1] uniformly randomly for i = 1 ... N-K+1 in orde... |
