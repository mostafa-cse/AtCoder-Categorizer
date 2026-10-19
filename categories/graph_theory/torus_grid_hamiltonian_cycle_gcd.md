# Hamiltonian Path and Cycle

**Taxonomy Path**: `Graph Theory` > `Hamiltonian Path` > `Hamiltonian Path and Cycle`

## Description
This topic focuses on hamiltonian path and cycle techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Since the rabbit visits all HW cells in HW steps, it visits each cell exactly once. Let R be the number of right moves and D be the number of down moves, with R + D = HW. The sequence of coordinates visited forms a single connected cycle of length HW on the torus if and only if gcd(R, W) = 1 and gcd(D, H) = 1. By Burnside's Lemma / cycle decomposition, any valid step choices must cover the torus grid evenly. This allows counting valid sequences using gcd factorization and modular binomial combinations.
- Common Reductions: A rabbit starts at (0, 0) on an H x W torus grid and repeatedly moves either 1 step down or 1 step right (both wrap around). Find the number of valid move sequences of length HW that visit all HW squares exactly once (forming a Hamiltonian cycle) modulo 10^9+7.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc046_d`](../../analysis/AtCoder-arc046_d.md) | D - うさぎとマス目 | 2852 | A rabbit starts at (0, 0) on an H x W torus grid and repeatedly moves either 1 step down or 1 step right (both wrap arou... |
