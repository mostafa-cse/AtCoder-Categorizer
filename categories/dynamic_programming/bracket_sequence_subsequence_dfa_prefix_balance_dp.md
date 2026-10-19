# Digit DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Digit DP` > `Digit DP`

## Description
This topic focuses on digit dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Valid bracket sequences prefer ')' over '(' for lexicographical maximality. Decompose S into a copies of '()' followed by b prime/splendid bracket sequences (where the first is not '()'). If S = ()^{K/2}, T needs only contain S as a subsequence, yielding sum_{j=K}^N C(j-1, K-1) 2^{N-j}. Otherwise, analyzing the insertion positions of '(' and ')' into the prime components yields rational generating functions: b x^2 / (1-x)^{2a+b+3} for >= 1 insertions, and (b x + 1) / (1-x)^{2a+b+2} for 0 insertions. Extracting coefficients via negative binomial expansion solves the problem in O(1) or O(N) time.
- Common Reductions: Given N, K and a valid bracket sequence S of length K, count strings T of length N whose lexicographically largest valid bracket subsequence of length K is S modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc071_b`](../../analysis/AtCoder-agc071_b.md) | B - Maximum Bracket Subsequence | 2842 | Given N, K and a valid bracket sequence S of length K, count strings T of length N whose lexicographically largest valid... |
