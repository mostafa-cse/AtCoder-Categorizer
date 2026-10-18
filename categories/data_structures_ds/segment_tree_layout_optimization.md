# Segment Tree (Point Update Range Query)

**Taxonomy Path**: `Data Structures (DS)` > `Segment Tree` > `Segment Tree (Point Update Range Query)`

## Description
This topic focuses on segment tree (point update range query) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Only the distinct query endpoints across the Q intervals can be branch split points. Let s be the number of distinct query endpoints (cut points), where s <= min(N - 1, 2Q). The minimum possible maximum depth of any such binary tree is d = floor(log2(s)) + 1. Within this depth bound, nodes at depth d - 1 can either be leaves or have 2 children at depth d. The number of partitions placed at depth d is t = s - (2^(d-1) - 1). We minimize the sum of query traversal costs by selecting t independent non-adjacent cut points to push to depth d via dynamic programming.
- Common Reductions: Minimizing the maximum depth and total search operations of a segment tree layout with N leaves and Q interval queries reduces to an optimal binary search tree partition over the set of distinct query boundary cuts.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc164_e`](../../analysis/AtCoder-arc164_e.md) | Segment-Tree Optimization | 2651 | Minimizing the maximum depth and total search operations of a segment tree layout with N leaves and Q interval queries r... |
