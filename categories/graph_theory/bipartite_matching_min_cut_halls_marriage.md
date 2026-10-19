# Maximum Flow / Minimum Cut

**Taxonomy Path**: `Graph Theory` > `Flow and Min Cut` > `Maximum Flow / Minimum Cut`

## Description
This topic focuses on maximum flow / minimum cut techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By the Max-Flow Min-Cut Theorem, maximum flow equals minimum s-t cut. In the bipartite flow network, let X_1 be the subset of left vertices cut to the source (paying sum_{i in X_1} A_i). If C = sum_{i in X_1} i, the residual capacity from X_1 to each right vertex j is C * j. Thus, each right vertex j contributes min(B_j, C * j) to the cut. The cut capacity for a chosen X_1 depends solely on C: Cut(X_1) = sum_{i in X_1} A_i + sum_{j=1}^M min(B_j, C * j). Since C <= N*(N+1)/2 <= 125,250, we can compute the minimum sum of A_i for each sum C using 0-1 knapsack DP, and precompute F(C) = sum_j min(B_j, C * j) using piecewise-linear prefix sum slopes.
- Common Reductions: Given N ball types with supply A_i, and M box types with capacity B_j, at most i * j balls of type i can be placed into boxes of type j. Find the maximum total number of balls that can be placed.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc332_g`](../../analysis/AtCoder-abc332_g.md) | G - Not Too Many Balls | 2775 | Given N ball types with supply A_i, and M box types with capacity B_j, at most i * j balls of type i can be placed into ... |
