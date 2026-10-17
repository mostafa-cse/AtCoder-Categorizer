# Number Theoretic Transform (NTT)

**Taxonomy Path**: `Math` > `Convolution` > `Number Theoretic Transform (NTT)`

## Description
This topic focuses on number theoretic transform (ntt) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If any value appears >= 4 times, capping its frequency to 3 preserves existence of a solution. With frequencies capped at 3, polynomial self-convolution f * f has coefficients at most 3 * 3 * X << 998244353, allowing standard NTT modulo 998244353 without overflow. From f * f, we obtain g(n) = number of pairs (t, u) with t < u and A_t + A_u = n. For any candidate s, the number of pairs (t, u) disjoint from s summing to X - A_s is g(X - A_s) - [f(X - 2A_s) - [X == 3A_s]]. We can check all s in O(N) and recover t, u in O(X).
- Common Reductions: Find an index triple 1 <= i < j < k <= N such that A_i + A_j + A_k = X, where N, X <= 10^6.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc185_c`](../../analysis/AtCoder-arc185_c.md) | Sum of Three Integers | 2242 | Find an index triple 1 <= i < j < k <= N such that A_i + A_j + A_k = X, where N, X <= 10^6.... |
