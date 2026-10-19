# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By tail probability integration, E[Y] = int_0^infty P(Y >= t) dt. The event that the K-th largest variable is >= t occurs iff at least K variables satisfy X_i >= t. For any t, p_i(t) = P(X_i >= t) is piecewise linear. Sorting all 2N endpoints {L_i, R_i} partitions the domain into intervals where each p_i(t) is a linear polynomial. Within each interval, the probability generating function prod (1 - p_i(t) + p_i(t) * x) has polynomial coefficients in t, which can be integrated analytically in closed form.
- Common Reductions: Given N independent uniform random variables X_i ~ U(L_i, R_i), compute the expected value of their K-th largest element modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc226_h`](../../analysis/AtCoder-abc226_h.md) | H - Random Kth Max | 2813 | Given N independent uniform random variables X_i ~ U(L_i, R_i), compute the expected value of their K-th largest element... |
