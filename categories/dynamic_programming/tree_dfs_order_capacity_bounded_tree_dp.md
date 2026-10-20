# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each ball (S_j, T_j) imposes routing constraints at lca(S_j, T_j): if lca is distinct from S_j and T_j, the child containing S_j must be visited before the child containing T_j. Furthermore, the optimal pickup/dropoff points along tree edges are fixed. For any vertex, the change in basket contents during subtree traversal is invariant, so the basket count upon entering vertex i is unique. Tree DP with memoized recursion counts valid branch orderings.
- Common Reductions: In a binary tree of N vertices with basket capacity K, count DFS traversals (choices of child visit orders) that allow delivering M balls from start to target without exceeding capacity.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc329_g`](../../analysis/AtCoder-abc329_g.md) | G - Delivery on Tree | 2995 | In a binary tree of N vertices with basket capacity K, count DFS traversals (choices of child visit orders) that allow d... |
