# Interval DP / Range DP / Matrix Chain Multiplication (MCM)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Classic DP` > `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`

## Description
This topic focuses on interval dp / range dp / matrix chain multiplication (mcm) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because H, W <= 6 and T <= 36, the number of distinct subrectangle sums is at most 441. Fixing the lower bound X converts the problem into finding the minimum possible maximum piece sum under the constraint that every cut piece has sum >= X.
- Common Reductions: Cut an H x W grid into T+1 rectangular pieces with straight cuts to minimize (max_piece - min_piece). Fix the minimum piece size X from the O(H^2 W^2) possible subrectangle sums and minimize the maximum piece size with range-based 2D MCM DP.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc298_g`](../../analysis/AtCoder-abc298_g.md) | G. Strawberry War | 2405 | Cut an H x W grid into T+1 rectangular pieces with straight cuts to minimize (max_piece - min_piece). Fix the minimum pi... |
