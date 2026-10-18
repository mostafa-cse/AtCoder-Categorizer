# Virtual Tree / Auxiliary Tree

**Taxonomy Path**: `Graph Theory` > `More Tree Stuff` > `Virtual Tree / Auxiliary Tree`

## Description
This topic focuses on virtual tree / auxiliary tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: When traversing child $v$ of vertex $u$ with color $c$, the size of the monochromatic component in $v$'s subtree bounded by color $c$ is $sz[v] - \Delta color\_sum[c]$, where $\Delta color\_sum[c]$ is the sum of subtrees of top occurrences of color $c$ inside $v$. Each component of size $S$ contributes $\frac{S(S+1)}{2}$ paths avoiding color $c$.
- Common Reductions: For each color $k$, count tree paths visiting at least one vertex of color $k$. Use complement counting: total paths $\frac{N(N+1)}{2}$ minus paths completely avoiding color $k$. Deleting all vertices of color $k$ decomposes the tree into monochromatic components of non-$k$ vertices. Subtree sizes maintained during a single post-order DFS determine the size of each monochromatic component in $O(N)$ total time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc163_f`](../../analysis/AtCoder-abc163_f.md) | F. path pass i | 2470 | For each color $k$, count tree paths visiting at least one vertex of color $k$. Use complement counting: total paths $\f... |
