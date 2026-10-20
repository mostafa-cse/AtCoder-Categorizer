# Contribution Technique

**Taxonomy Path**: `Combinatorics` > `Techniques` > `Contribution Technique`

## Description
This topic focuses on contribution technique techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Fix person 0 to be chosen, then multiply total cost by L/N. Compute c[d], the number of choices where maximum distance <= d. Points must lie in [-d, d]. Choosing points on the left [1, d-1] (red points) and right [L-d+1, L-1] (blue intervals of length W = L - 2d + 1) such that no red point falls in a blue interval. Classifying by the number of alternations i between red and blue components allows direct closed-form binomial coefficient evaluation: sum_i binom(d - i(W - 2), N - 1) binom(N, 2i + 1). Summing across d takes harmonic series time O(L log L).
- Common Reductions: Choose N people out of L on a circle. The cost is the maximum pairwise circular distance. Find the sum of costs over all binom(L, N) subsets, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc068_a`](../../analysis/AtCoder-agc068_a.md) | A. Circular Distance | 2948 | Choose N people out of L on a circle. The cost is the maximum pairwise circular distance. Find the sum of costs over all... |
