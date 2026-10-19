# Grundy Number and Basic Game Theory

**Taxonomy Path**: `Game Theory` > `Grundy Number / Nim` > `Grundy Number and Basic Game Theory`

## Description
This topic focuses on grundy number and basic game theory techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Exponential weights force greedy lexicographical choice: a vertex is selected iff none of its higher-indexed neighbors are selected. Orienting edges u -> v for u < v creates a DAG, and the greedy independent set is precisely the kernel (P-positions / Grundy value 0) of the game on W. Since W is the independent sum of games on X, Y, Z, the Sprague-Grundy theorem gives g_W(i, j, k) = g_X(i) ^ g_Y(j) ^ g_Z(k) = 0. Factorizing weights into S_X, S_Y, S_Z by Grundy value allows summing over g_1 ^ g_2 ^ g_3 = 0 in O(G^2) time.
- Common Reductions: Three graphs X, Y, Z on N vertices form a Cartesian product graph W with N^3 vertices (i, j, k) having exponential weights 10^{18(i+j+k)}. Find the maximum weight independent set in W modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc043_c`](../../analysis/AtCoder-agc043_c.md) | C - Giant Graph | 2872 | Three graphs X, Y, Z on N vertices form a Cartesian product graph W with N^3 vertices (i, j, k) having exponential weigh... |
