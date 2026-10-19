# Bitmask DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Bit Related DP` > `Bitmask DP`

## Description
This topic focuses on bitmask dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Decompose x = u * 2^a 3^b with gcd(u, 6) = 1. The problem decouples independently for each u <= N. For each u, we must cover the 2D lattice shape P(M) = {(a, b) | 2^a 3^b <= floor(N / u)}. There are only 306 distinct shapes P(M). Covering a shape is a minimum dominating set on the 2D multiplicative poset grid, solved via bitmask DP with superset Fast Zeta Transform (SOS DP).
- Common Reductions: Given N <= 10^9, operation chooses x and adds x, 2x, 3x to set S. Find the minimum operations so {1, 2, ..., N} subset S.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc184_b`](../../analysis/AtCoder-arc184_b.md) | B - 123 Set | 2867 | Given N <= 10^9, operation chooses x and adds x, 2x, 3x to set S. Find the minimum operations so {1, 2, ..., N} subset S... |
