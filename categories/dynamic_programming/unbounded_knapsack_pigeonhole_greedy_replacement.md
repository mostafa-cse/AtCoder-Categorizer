# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Let i' be the item maximizing density B_i / D_i. Any collection of non-i' items with total weight >= K(K + 1) has a subset of items whose weight sum is a multiple of D_{i'}, which can be replaced by i' without decreasing the value. Therefore, knapsack DP only needs to be run up to K(K + 1) approx 96,000, and all remaining capacity is filled greedily using item i'.
- Common Reductions: Given N <= 10^{15} initial colas, exchange recipes (A_i, B_i) consume D_i = A_i - B_i empty bottles for B_i new colas with A_i, B_i <= 300. Maximize total colas drunk. The unbounded knapsack structure allows pruning non-maximal items and reducing the DP domain via the Pigeonhole Principle.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc415_g`](../../analysis/AtCoder-abc415_g.md) | G. Get Many Cola | 2180 | Given N <= 10^{15} initial colas, exchange recipes (A_i, B_i) consume D_i = A_i - B_i empty bottles for B_i new colas wi... |
