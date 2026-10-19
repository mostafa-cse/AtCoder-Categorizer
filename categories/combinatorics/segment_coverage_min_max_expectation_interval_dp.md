# Principle of Inclusion and Exclusion (PIE)

**Taxonomy Path**: `Combinatorics` > `Inclusion Exclusion` > `Principle of Inclusion and Exclusion (PIE)`

## Description
This topic focuses on principle of inclusion and exclusion (pie) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By Min-Max Expectation, E[max T_i] = sum_{empty != S} (-1)^{|S|+1} E[min_{i in S} T_i]. The time to hit at least one cell in S is a geometric random variable with expectation M / c(S), where c(S) is the number of intervals intersecting S. Crucially, c(S) = M - (intervals disjoint from S). For a chosen subset S = {s_1 < ... < s_k}, an interval is disjoint from S iff it lies entirely within one gap [s_j + 1, s_{j+1} - 1]. An interval DP computes the signed weights sum_{S: c(S) = c} (-1)^{|S|+1} in O(N^2 M) time.
- Common Reductions: N cells initially white. M intervals [L_i, R_i] in a box. In each step, draw a random interval and paint its cells black. Find the expected number of steps until all N cells are black modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc242_h`](../../analysis/AtCoder-abc242_h.md) | Ex - Random Painting | 2835 | N cells initially white. M intervals [L_i, R_i] in a box. In each step, draw a random interval and paint its cells black... |
