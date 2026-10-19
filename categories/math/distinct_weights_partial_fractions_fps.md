# Generating Functions

**Taxonomy Path**: `Math` > `Polynomial` > `Generating Functions`

## Description
This topic focuses on generating functions techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The ordinary generating function for card i is sum_{j=0}^{B_i} (A_i x)^j = (1 - (A_i x)^{B_i + 1}) / (1 - A_i x). The total generating function is F(x) = prod_{i=1}^N (1 - (A_i x)^{B_i + 1}) / prod_{i=1}^N (1 - A_i x). Expanding the numerator yields at most 2^N terms (-1)^{|S|} prod_{i in S} A_i^{B_i+1} x^{sum_{i in S} (B_i+1)}. The denominator 1 / prod_{i=1}^N (1 - A_i x) decomposes by partial fractions into sum_{i=1}^N c_i / (1 - A_i x), where c_i = prod_{j != i} 1 / (1 - A_j / A_i). The coefficient of x^k in 1 / (1 - A_i x) is A_i^k. Thus, each monomial c * x^L in the numerator contributes c * sum_{i=1}^N c_i A_i^{M - L} to [x^M] F(x).
- Common Reductions: Given N distinct card types with values A_i and limits B_i, count the sum of products of chosen card values over all multisets of size M modulo 998244353, where M can be up to 10^18 and N <= 16.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc241_h`](../../analysis/AtCoder-abc241_h.md) | Ex. Card Deck Score | 2881 | Given N distinct card types with values A_i and limits B_i, count the sum of products of chosen card values over all mul... |
