# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In a full binary tree where every internal node has 2 children, edge counts satisfy E(XX) + E(XY) + E(YX) + E(YY) = N - 1. Using tree DP, the set of achievable counts of (Y_count, XY_count) in each subtree forms a contiguous interval. We compute bottom-up reachable intervals for each node conditioned on its parent's label, check feasibility at the root, and backtrack top-down to construct the string.
- Common Reductions: Given a full binary tree with N vertices, determine if there exists an assignment of labels 'X' or 'Y' to each vertex with exactly A vertices labeled 'Y', B edges labeled 'XX', and C edges labeled 'XY', and construct one if possible.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc157_e`](../../analysis/AtCoder-arc157_e.md) | E. XXYX Binary Tree | 2877 | Given a full binary tree with N vertices, determine if there exists an assignment of labels 'X' or 'Y' to each vertex wi... |
