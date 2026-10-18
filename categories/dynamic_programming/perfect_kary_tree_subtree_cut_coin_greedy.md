# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A perfect K-ary tree of height h has V_h = (K^{h+1}-1)/(K-1) vertices. To reduce it to X vertices, we must remove exactly V_h - X vertices using complete subtrees of heights 0, 1, ..., h-1. Because the subtree sizes satisfy the canonical coin system criteria, the greedy choice of the largest possible subtree is strictly optimal.
- Common Reductions: Cut edges in a perfect K-ary tree of depth D to obtain a connected component of exactly X vertices with the minimum number of cuts. Fixing the component's root at height h reduces the problem to an exact-change coin change problem with canonical tree sizes V_i.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc290_g`](../../analysis/AtCoder-abc290_g.md) | G. Edge Elimination | 2407 | Cut edges in a perfect K-ary tree of depth D to obtain a connected component of exactly X vertices with the minimum numb... |
