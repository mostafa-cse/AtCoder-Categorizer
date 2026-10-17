# Depth First Search (DFS)

**Taxonomy Path**: `Graph Theory` > `Graph Traversal` > `Depth First Search (DFS)`

## Description
This topic focuses on depth first search (dfs) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The problem guarantees a consistent multiplicative system where the maximum conversion factor fits in a 64-bit integer <= 10^9. Rooting the tree at an arbitrary vertex with reference potential 1.0 and propagating ratios pot[v] = pot[u] / m for edge 1 u = m v allows finding the maximum potential unit (largest) and minimum potential unit (smallest) via DFS.
- Common Reductions: Given N <= 200 unit conversion rules 1 large = m small, find the largest unit and smallest unit that maximize the conversion factor M, and output 1large=Msmall. Unit conversions form a connected multiplicative tree.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc015_3`](../../analysis/AtCoder-arc015_3.md) | C. 変わった単位 | 2185 | Given N <= 200 unit conversion rules 1 large = m small, find the largest unit and smallest unit that maximize the conver... |
