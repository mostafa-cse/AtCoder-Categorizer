# Divide and Conquer Optimization

**Taxonomy Path**: `Dynamic Programming (DP)` > `DP Optimizations` > `Divide and Conquer Optimization`

## Description
This topic focuses on divide and conquer optimization techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For each ticket type j, restaurant i provides the maximum deliciousness B_{i, j} over a maximal interval [L_i, R_i], computable using a monotonic stack. Thus, restaurant i contributes B_{i, j} to all query intervals [l, r] satisfying L_i <= l <= i and i <= r <= R_i. This contribution is a 2D rectangle in the (l, r) plane. Applying 2D difference array updates for all N * M rectangles across all tickets takes O(N * M) time. Computing the 2D prefix sums takes O(N^2) time, immediately yielding the optimal interval in O(N * M + N^2) total time.
- Common Reductions: There are N restaurants on a line with distances A_i between adjacent restaurants, and M meal tickets. Restaurant i gives deliciousness B_{i, j} for ticket j. Find the maximum happiness sum_{j=1}^M max_{k in [L, R]} B_{k, j} - dist(L, R) over all intervals 1 <= L <= R <= N.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc067_d`](../../analysis/AtCoder-arc067_d.md) | F - Yakiniku Restaurants | 2729 | There are N restaurants on a line with distances A_i between adjacent restaurants, and M meal tickets. Restaurant i give... |
