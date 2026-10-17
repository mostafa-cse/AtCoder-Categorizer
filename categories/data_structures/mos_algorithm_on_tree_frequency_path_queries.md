# Mo's on Tree

**Taxonomy Path**: `Data Structures (DS)` > `Square Root Decomposition` > `Mo's on Tree`

## Description
This topic focuses on mo's on tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Flatten the tree via Euler tour of length 2N recording enter and exit times. Path between s and t translates to interval [tout[s], tin[t]] (plus LCA if lca != s) where vertices occurring odd times lie on the path. Mo's algorithm maintains frequency of each color: when color count updates, maintaining g[k] = count of colors with frequency >= k allows O(1) frequency transitions and O(1) range queries via g[a] - g[b+1].
- Common Reductions: Given a tree with vertex values, answer Q path queries (s, t, a, b) asking for the number of distinct values y whose frequency on the path satisfies a <= freq(y) <= b.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc477_g`](../../analysis/AtCoder-abc477_g.md) | Frequency Query on Tree | 2226 | Given a tree with vertex values, answer Q path queries (s, t, a, b) asking for the number of distinct values y whose fre... |
