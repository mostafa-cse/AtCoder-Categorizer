# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A perfect binary tree of depth d has 2^d - 1 vertices, so maximum depth is at most 19 for N <= 3*10^5. Adding vertex k only introduces a leaf of depth 1, which propagates up the tree to ancestors at distance h altering only their DP value at depth h+1. Using e_2(S) = (sum(S)^2 - sum(S^2))/2, each ancestor update runs in O(1), bounding the update cost per vertex to at most 19 steps.
- Common Reductions: Track perfect binary trees of depth d rooted at vertex 1 incrementally as vertices are added by maintaining the elementary symmetric polynomial of degree 2 over children's DP values up to maximum depth 19.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc264_h`](../../analysis/AtCoder-abc264_h.md) | Perfect Binary Tree | 2660 | Track perfect binary trees of depth d rooted at vertex 1 incrementally as vertices are added by maintaining the elementa... |
