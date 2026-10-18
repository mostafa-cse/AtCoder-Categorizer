# Knapsack and Subset Sum Optimizations

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Subset Sum Optimizations`

## Description
This topic focuses on knapsack and subset sum optimizations techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any convex sequence is uniquely determined by its leftmost minimum at index m, plus a flat base of weight N, rays of weights k(k+1)/2 to the left (requiring ray m-1 at least once if m > 1), and rays of weights j(j+1)/2 to the right. Since weights grow quadratically, only at most sqrt(2M) <= 450 distinct item weights can ever be used.
- Common Reductions: Count the number of non-negative integer sequences A of length N summing to M such that 2 A_i <= A_{i-1} + A_{i+1} for all 2 <= i <= N-1 (convexity), modulo 10^9+7.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc049_d`](../../analysis/AtCoder-agc049_d.md) | D. Convex Sequence | 2602 | Count the number of non-negative integer sequences A of length N summing to M such that 2 A_i <= A_{i-1} + A_{i+1} for a... |
