# Convex Hull Trick (CHT) and Dynamic CHT

**Taxonomy Path**: `Dynamic Programming (DP)` > `Convex Hull Trick (CHT)` > `Convex Hull Trick (CHT) and Dynamic CHT`

## Description
This topic focuses on convex hull trick (cht) and dynamic cht techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Binary search on time v. Person i and person j can meet within time v iff their initial distance is at most 2v. In optimal movement, people meet in contiguous pair or triplet groups. Transitioning from i to j requires A[j] - A[i+1] <= 2v. A difference array or prefix-sum DP verifies feasibility in O(N) time per binary search iteration.
- Common Reductions: Finding the minimum time for all N people on a line to meet reduces via binary search on time v to checking whether an interval-chain dynamic programming transition can connect person 1 to person N.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc120_e`](../../analysis/AtCoder-arc120_e.md) | 1D Party | 2653 | Finding the minimum time for all N people on a line to meet reduces via binary search on time v to checking whether an i... |
