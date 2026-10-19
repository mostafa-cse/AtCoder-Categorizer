# Knapsack and Subset Sum Optimizations

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Subset Sum Optimizations`

## Description
This topic focuses on knapsack and subset sum optimizations techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Rotate coordinates by 45 degrees: let u = x + y and v = x - y. Each step of length D changes (u, v) by (+/-D, +/-D) where the signs for u and v are completely independent! The 2D reachability problem decouples into two independent 1D subset sum problems: choose signs for u to reach A + B, and signs for v to reach A - B. Subset sum with bitset optimization determines reachability and enables exact path reconstruction.
- Common Reductions: Starting at (0, 0), make N jumps of lengths D_1, ..., D_N in directions (U, D, L, R). Determine if (A, B) is reachable, and reconstruct the path if possible.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc221_g`](../../analysis/AtCoder-abc221_g.md) | G. Jumping sequence | 2914 | Starting at (0, 0), make N jumps of lengths D_1, ..., D_N in directions (U, D, L, R). Determine if (A, B) is reachable, ... |
