# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By symmetry, assume A <= B. A string is reachable if and only if replacing all runs of 0s of length >= A with 1s produces at least one run of 1s of length >= B. We count invalid strings (those that do not produce any run of 1s of length >= B) using dynamic programming. In an invalid string, surviving 0-runs have length < A (acting as delimiters of length 1..A-1), and the segments between delimiters must have length L < B and contain only 0-runs of length >= A. Precomputing the number of such segments of length L via 1D DP allows computing the total invalid strings in O(N^2) time.
- Common Reductions: Starting from an all-zero string of length N, we can choose A consecutive characters and replace them with 0, or choose B consecutive characters and replace them with 1, any number of times. Find the number of reachable strings modulo 10^9 + 7.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc045_c`](../../analysis/AtCoder-agc045_c.md) | C - Range Set | 2758 | Starting from an all-zero string of length N, we can choose A consecutive characters and replace them with 0, or choose ... |
