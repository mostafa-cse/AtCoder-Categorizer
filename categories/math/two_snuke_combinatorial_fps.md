# Generating Functions

**Taxonomy Path**: `Math` > `Polynomial` > `Generating Functions`

## Description
This topic focuses on generating functions techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The combinatorial state space can be decomposed using generating functions into S(t) = t^5 / ((1 + t)^5 * (1 - t)^16). Expanding this rational function shows that the coefficient [t^N] S(t) splits into two polynomials in N of degree 15: one for even N and one for odd N. Because the degree is only 15, we can precompute the first 35 coefficients directly using formal power series truncated division, and then use Lagrange interpolation in O(d) time (d = 15) to evaluate the polynomial at N.
- Common Reductions: Two players simultaneously place points in a bounded region defined by linear constraints related to N, summing up values depending on geometric placements. Find the expected/total score modulo 998244353 for N <= 10^9.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-aising2020_f`](../../analysis/AtCoder-aising2020_f.md) | F - Two Snuke | 2741 | Two players simultaneously place points in a bounded region defined by linear constraints related to N, summing up value... |
