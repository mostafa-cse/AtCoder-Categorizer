# Segment Tree (Point Update Range Query)

**Taxonomy Path**: `Data Structures (DS)` > `Segment Tree` > `Segment Tree (Point Update Range Query)`

## Description
This topic focuses on segment tree (point update range query) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Average performance at contest n is >= B iff sum_{i=1}^n (a_i - B) >= 0. Defining b_i = a_i - B, the rating freezes at the smallest prefix index n with prefix_sum(b, n) >= 0. We can maintain sum and max_prefix_sum in a Segment Tree over b_i. A walk on the Segment Tree in O(log N) identifies the first index n where prefix sum >= 0.
- Common Reductions: Maintain performance estimates under point updates and report final rating, where rating freezes at the first contest where average performance reaches at least B.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc292_h`](../../analysis/AtCoder-abc292_h.md) | Rating Estimator | 2248 | Maintain performance estimates under point updates and report final rating, where rating freezes at the first contest wh... |
