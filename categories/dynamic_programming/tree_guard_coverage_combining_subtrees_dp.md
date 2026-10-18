# Combining Subtrees Technique

**Taxonomy Path**: `Dynamic Programming (DP)` > `More Tricks` > `Combining Subtrees Technique`

## Description
This topic focuses on combining subtrees technique techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In tree DP counting guard placements covering exactly K vertices, each vertex u requires 3 states: 0 (no guard, unguarded), 1 (guard placed at u, self and neighbors guarded), 2 (no guard at u, guarded by a child). Subtree merges run in O(size(u) * size(v)), bounding total complexity to O(N^2) by the tree knapsack theorem.
- Common Reductions: Tree DP with 3 states per node (unguarded, guard placed, guarded by child) counts covered vertices. Merging subtrees via tree knapsack bounds total operations to O(N^2).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc207_f`](../../analysis/AtCoder-abc207_f.md) | F. Tree Patrolling | 2398 | Tree DP with 3 states per node (unguarded, guard placed, guarded by child) counts covered vertices. Merging subtrees via... |
