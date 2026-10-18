# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: When merging child $v$ into $u$, if $u$ is a local maximum ($v < u$), $v$ must precede $u$ in the merged ordering, meaning the rank of $v$ in its own subtree is bounded by the number of elements allocated from $v$'s subtree before $u$. This evaluates to a prefix sum over $dp[v]$.
- Common Reductions: Count permutations of vertices on a tree where every vertex is a local extremum. Because trees are bipartite, the vertices alternate between local minima and local maxima, directing all edges. Reversing the permutation ($P'_i = N + 1 - P_i$) shows that both 2-colorings yield an identical number of linear extensions. Tree DP maintaining subtree relative rank $dp[u][r]$ with prefix/suffix sums merges subtrees in $O(N^2)$ total time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc130_d`](../../analysis/AtCoder-arc130_d.md) | D. Zigzag Tree | 2437 | Count permutations of vertices on a tree where every vertex is a local extremum. Because trees are bipartite, the vertic... |
