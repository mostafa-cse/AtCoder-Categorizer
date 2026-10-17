# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each edge requires L_u >= L_v - 1 and R_u <= R_v + 1. If interval intersection [L_u, R_u] is non-empty and parity is globally consistent, valid assignments val[v] in {val[u] - 1, val[u] + 1} are guaranteed to exist.
- Common Reductions: Fill empty tree vertices so adjacent vertices differ by exactly 1, given K pre-assigned vertices. Bipartiteness enforces that (val[u] - depth[u]) mod 2 must be identical for all fixed vertices. A bottom-up DP intersects valid intervals [L_u, R_u], and a top-down greedy pass assigns consistent values in O(N) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc063_c`](../../analysis/AtCoder-arc063_c.md) | E. Integers on a Tree | 2198 | Fill empty tree vertices so adjacent vertices differ by exactly 1, given K pre-assigned vertices. Bipartiteness enforces... |
