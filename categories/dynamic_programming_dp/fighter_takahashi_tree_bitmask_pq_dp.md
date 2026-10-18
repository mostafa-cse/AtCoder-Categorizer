# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Greedy rule: Always defeat all currently defeatable enemies before consuming any medicine (addition before multiplication strictly dominates). Since there are at most $K \le 10$ medicines, perform bitmask DP over the subset of consumed medicines. From state $mask$, greedily expand reachable enemies via a min-priority queue, then transition to $mask \mid (1 \ll m)$ for each accessible medicine $m$.
- Common Reductions: Explore a rooted tree with enemies (add strength $g_u$ if $\ge s_u$) and $\le 10$ medicines (multiply strength by $g_u$). Determine if all enemies can be defeated.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc319_f`](../../analysis/AtCoder-abc319_f.md) | F. Fighter Takahashi | 2480 | Explore a rooted tree with enemies (add strength $g_u$ if $\ge s_u$) and $\le 10$ medicines (multiply strength by $g_u$)... |
