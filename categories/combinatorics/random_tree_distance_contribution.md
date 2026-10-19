# Contribution Technique

**Taxonomy Path**: `Combinatorics` > `Techniques` > `Contribution Technique`

## Description
This topic focuses on contribution technique techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By linearity of expectation, E[d(u, v)] = E[depth(u)] + E[depth(v)] - 2 * E[depth(LCA(u, v))]. First, expected depths satisfy E_1 = 0 and E_v = A_v + (1 / (v-1)) * sum_{i=1}^{v-1} E_i for 2 <= v <= N, computable in O(N) using prefix sums. Second, remarkably, for u < v, the distribution of LCA(u, v) depends ONLY on u, not on v! Specifically, moving up from v, the first node <= u is uniformly distributed on 1..u with probability 1/u. This yields L_u = E[depth(LCA(u, v))] = (1 / u) * (E_u + sum_{i=1}^{u-1} L_i), computable in O(N). Each query is then answered in O(1) as (E_u + E_v - 2*L_u) * (N - 1)! mod 998244353.
- Common Reductions: A tree on N vertices rooted at 1 is formed by independently choosing parent P_i uniformly from 1..i-1 with edge weight A_i for each i in 2..N. There are (N - 1)! possible trees. For Q queries (u, v), find the sum of distances between u and v across all trees modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc195_e`](../../analysis/AtCoder-arc195_e.md) | E - Random Tree Distance | 2734 | A tree on N vertices rooted at 1 is formed by independently choosing parent P_i uniformly from 1..i-1 with edge weight A... |
