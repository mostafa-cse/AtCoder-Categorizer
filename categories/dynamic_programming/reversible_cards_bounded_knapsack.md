# Knapsack and Subset Sum Optimizations

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Subset Sum Optimizations`

## Description
This topic focuses on knapsack and subset sum optimizations techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because the sum of absolute deltas is bounded by $M$, grouping identical deltas and applying binary powers of 2 reduces the number of items to at most $O(\sqrt{M} \log M)$, easily processed by 0-1 knapsack DP.
- Common Reductions: Given $N$ cards with front $A_i$ and back $B_i$ such that $\sum (A_i + B_i) = M \le 200000$, find the minimum flips to achieve sum $k$ for each $k \in [0, M]$. The initial sum is $S_0 = \sum A_i$, and flipping card $i$ changes the sum by $\Delta_i = B_i - A_i$. Since $\sum |\Delta_i| \le M$, there are at most $O(\sqrt{M})$ distinct non-zero deltas. Binary splitting converts this into a bounded knapsack problem solvable in $O(M \sqrt{M})$ time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc269_g`](../../analysis/AtCoder-abc269_g.md) | G. Reversible Cards 2 | 2440 | Given $N$ cards with front $A_i$ and back $B_i$ such that $\sum (A_i + B_i) = M \le 200000$, find the minimum flips to a... |
