# DSU on Tree and Small to Large Merging

**Taxonomy Path**: `Data Structures (DS)` > `Disjoint Set Union (DSU)` > `DSU on Tree and Small to Large Merging`

## Description
This topic focuses on dsu on tree and small to large merging techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: With $N = 2.5 \times 10^6$, map-based small-to-large merging is too slow due to pointer and dynamic allocation overhead. DSU on Tree (Sack) using a single flat frequency array $cnt$ allows $O(N \log N)$ total time with tiny constant factor.
Crucially, during the heavy-light traversal, when processing light children with `keep = false`, the entire subtree is wiped back to zero, allowing mode tracking without maintaining reverse frequency buckets.
- Common Reductions: Given a rooted tree of $N$ colored vertices ($N \le 2.5 \times 10^6$), for each vertex $v$, find the maximum frequency $m_v$ of any color in $v$'s subtree and the count $k_v$ of colors achieving that maximum frequency. Output $\sum (m_i \oplus i)(k_i \oplus i) \bmod 998244353$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc454_g`](../../analysis/AtCoder-abc454_g.md) | G. Mode in the Subtree | 2253 | Given a rooted tree of $N$ colored vertices ($N \le 2.5 \times 10^6$), for each vertex $v$, find the maximum frequency $... |
