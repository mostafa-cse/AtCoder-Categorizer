# Treap

**Taxonomy Path**: `Data Structures (DS)` > `Balanced Binary Search Tree (BBST)` > `Treap`

## Description
This topic focuses on treap techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The canonical merge condition P_{i+1} - P_i >= A causes inserted points to propagate shifts and mergers to subsequent points. Because the merge rule is associative, the canonicalized sequence can be maintained in blocks of sizes that are powers of 2 (or a randomized Treap / binary lifting table). Queries perform binary searches on each block to locate the effective position and compute mood contributions in O(log^2 M).
- Common Reductions: Takahashi maintains a sequence of present values under dynamic insertions and queries: an operation merges adjacent values if their difference is less than A, maintaining a canonical sparse sequence where P_{i+1} - P_i >= A. Compute Takahashi's expected mood across all query points.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc427_g`](../../analysis/AtCoder-abc427_g.md) | G - Takahashi's Expectation 2 | 2974 | Takahashi maintains a sequence of present values under dynamic insertions and queries: an operation merges adjacent valu... |
