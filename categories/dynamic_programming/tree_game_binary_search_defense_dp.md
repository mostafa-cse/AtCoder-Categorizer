# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: To prevent Takahashi from reaching any vertex with score $\ge X$, Aoki must spend at least $\max(0, \sum_{v \in children(u)} dp[v] - 1) + [A_u \ge X]$ moves within the subtree of $u$ before Takahashi enters $u$.
- Common Reductions: In a tree game on $N$ vertices with root 1 and values $A_i$, Takahashi moves a piece downward while Aoki zeroes out an unvisited vertex. Takahashi wants to maximize the final value; Aoki wants to minimize it. Determine Takahashi's optimal score.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc246_g`](../../analysis/AtCoder-abc246_g.md) | G. Game on Tree 3 | 2313 | In a tree game on $N$ vertices with root 1 and values $A_i$, Takahashi moves a piece downward while Aoki zeroes out an u... |
