# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In any valid two-coloring of the subtree rooted at $u$, one color has total weight $X_u$. To maximize feasibility for ancestor constraints, $dp[u]$ stores the minimum possible weight of the other color in subtree $u$.
- Common Reductions: In a tree where each node $u$ requires one color in its subtree to sum to $X_u$, determine if there exists a valid non-negative weight assignment and 2-coloring for all vertices.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc083_c`](../../analysis/AtCoder-arc083_c.md) | C. Bichrome Tree | 2289 | In a tree where each node $u$ requires one color in its subtree to sum to $X_u$, determine if there exists a valid non-n... |
