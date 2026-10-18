# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In an optimal tournament, the player with the larger $r$ always wins each match, leaving the losing player's $r$ at the match node (and both players' $r$ at the root). The linear programming dual of modifying $[l'_i, r'_i]$ to satisfy ancestor-descendant constraints is a maximum weight bipartite matching between leaf $l_v$ and match $r_u$ with weight $l_v - r_u$. Since each leaf can only match its ancestors and there are at most $N + 1$ ancestors, the number of unmatched leaves in any subtree is bounded by its ancestor depth, yielding a tree DP in $O(N 2^N)$ time.
- Common Reductions: Find the minimum cost to adjust player intervals $[l_i, r_i]$ so that a single-elimination tournament on $2^N$ players can complete its final.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc069_a`](../../analysis/AtCoder-agc069_a.md) | A - Schedule Optimization | 2460 | Find the minimum cost to adjust player intervals $[l_i, r_i]$ so that a single-elimination tournament on $2^N$ players c... |
