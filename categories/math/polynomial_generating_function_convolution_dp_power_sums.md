# Generating Functions

**Taxonomy Path**: `Math` > `Polynomial` > `Generating Functions`

## Description
This topic focuses on generating functions techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The problem is finding the coefficient of t^C in prod_{i=1}^N P_i(t). Precomputing power sum tables S(k, m) = sum_{x=1}^m x^k mod MOD in O(C * max_B) time allows evaluating interval power sums sum_{x=A_i}^{B_i} x^k = S(k, B_i) - S(k, A_i - 1) in O(1). Standard polynomial DP convolving one child at a time runs in O(N C^2) time.
- Common Reductions: Sum prod_{i=1}^N x_i^{c_i} over all x_i in [A_i, B_i] and all candy allocations sum_{i=1}^N c_i = C with c_i >= 0 modulo 10^9+7. The sum factorizes into polynomial convolution where child i has generating function P_i(t) = sum_{k=0}^C (sum_{x=A_i}^{B_i} x^k) t^k.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc059_c`](../../analysis/AtCoder-arc059_c.md) | E. Children and Candies | 2189 | Sum prod_{i=1}^N x_i^{c_i} over all x_i in [A_i, B_i] and all candy allocations sum_{i=1}^N c_i = C with c_i >= 0 modulo... |
