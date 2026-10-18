# Knapsack and Subset Sum Optimizations

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Subset Sum Optimizations`

## Description
This topic focuses on knapsack and subset sum optimizations techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: This is a knapsack and subset sum optimization. Because duration weights are structured and constraints can be formulated as resource capacity limits, we can optimize the standard O(N * W) DP using monotonicity and bitset/histogram acceleration.
- Common Reductions: Given N song candidates each with duration and popularity, select an optimal set of songs to maximize total popularity subject to maximum total performance duration and constraints on consecutive songs.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc424_g`](../../analysis/AtCoder-abc424_g.md) | G. Set list | 2552 | Given N song candidates each with duration and popularity, select an optimal set of songs to maximize total popularity s... |
