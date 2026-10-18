# Basic Greedy Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Greedy Algorithms`

## Description
This topic focuses on basic greedy algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: To maximize walking distance on a circle of length $L$, the traveler must alternate moving between the leftmost and rightmost unburned trees (crossing origin 0 each time to maximize step length). The optimal trajectory visits a prefix of $k$ trees from one direction and $N-k$ from the opposite, with strictly alternating steps at the end.
- Common Reductions: Find the maximum distance to burn all trees along a circular walk. The optimal path alternates visiting the leftmost and rightmost unburned trees, evaluated over all $N$ split points using prefix sums in $O(N)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc030_b`](../../analysis/AtCoder-agc030_b.md) | B. Tree Burning | 2342 | Find the maximum distance to burn all trees along a circular walk. The optimal path alternates visiting the leftmost and... |
