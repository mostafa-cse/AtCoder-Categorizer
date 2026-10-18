# Combining Subtrees Technique

**Taxonomy Path**: `Dynamic Programming (DP)` > `More Tricks` > `Combining Subtrees Technique`

## Description
This topic focuses on combining subtrees technique techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In each connected component, vertices can be deactivated or partitioned by cutting edges. For each subtree rooted at $u$, we maintain tree knapsack DP states: the minimum cuts to make all separated subtrees valid, distinguishing whether the connected component containing $u$ has a strictly positive sum ($dp_1$) or a negative/arbitrary sum ($dp_2$). Tree knapsack merging takes $O(N^2)$ total time.
- Common Reductions: Find the minimum number of edge removals in a vertex-weighted tree so that every connected component has a positive sum.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-aising2019_e`](../../analysis/AtCoder-aising2019_e.md) | E - Attack to a Tree | 2595 | Find the minimum number of edge removals in a vertex-weighted tree so that every connected component has a positive sum.... |
