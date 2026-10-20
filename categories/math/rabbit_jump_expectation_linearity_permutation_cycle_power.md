# Matrix Exponentiation

**Taxonomy Path**: `Math` > `Matrices` > `Matrix Exponentiation`

## Description
This topic focuses on matrix exponentiation techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By linearity of expectation, jumping across a neighbor updates expected coordinate to x'_i = x_{i-1} + x_{i+1} - x_i. Considering differences d_i = x_{i+1} - x_i, this jump simply swaps d_{i-1} and d_i! The entire sequence of M jumps is therefore a single permutation sigma on the difference array. Computing sigma^K via cycle decomposition in O(N) yields the exact final differences and positions.
- Common Reductions: N rabbits start at positions x_1 < ... < x_N. At each step, a chosen rabbit jumps across one of its neighbors with equal probability. Find expected final positions after repeating a pattern of M jumps K times.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc006_c`](../../analysis/AtCoder-agc006_c.md) | C - Rabbit Exercise | 2996 | N rabbits start at positions x_1 < ... < x_N. At each step, a chosen rabbit jumps across one of its neighbors with equal... |
