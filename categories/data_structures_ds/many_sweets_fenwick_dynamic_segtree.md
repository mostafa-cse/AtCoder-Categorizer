# 2D Dynamic Segment Tree

**Taxonomy Path**: `Data Structures (DS)` > `Segment Tree` > `2D Dynamic Segment Tree`

## Description
This topic focuses on 2d dynamic segment tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The problem requires dynamic 2D point additions and 2D prefix/rectangle aggregations. Because one coordinate has bounded range while the other is large, a Fenwick tree over the first coordinate where each node contains a dynamic segment tree over the second coordinate provides O(log^2 N) point updates and range queries without storing unnecessary empty nodes.
- Common Reductions: Given N boxes of sweets with weights and values, process Q queries where sweets can be bought subject to 2D range restrictions on coordinates and capacity constraints.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc467_g`](../../analysis/AtCoder-abc467_g.md) | G. Many Sweets Problem | 2544 | Given N boxes of sweets with weights and values, process Q queries where sweets can be bought subject to 2D range restri... |
