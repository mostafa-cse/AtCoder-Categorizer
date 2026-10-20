# Tree Diameter

**Taxonomy Path**: `Graph Theory` > `Graph Traversal` > `Tree Diameter`

## Description
This topic focuses on tree diameter techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The core structural property of long paths in a tree is governed by tree diameter and repeated leaf-stripping. The minimal intersection of all diameter-like paths collapses to a central path P*. If P* has length >= 2, any valid pair must have endpoints in the two opposite branch subtrees of P*. If P* is a single vertex, valid pairs branch out in different subtrees of this central centroid/diameter midpoint. This reduces the path count to polynomial convolutions of subtree depth profiles, evaluated via NTT.
- Common Reductions: Given a tree T with N <= 2 * 10^5 vertices, count pairs of vertices (u, v) such that their distance is >= D and the induced subgraph of their path satisfies structural degree bounds, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc215_f`](../../analysis/AtCoder-arc215_f.md) | F - Scapus | 2972 | Given a tree T with N <= 2 * 10^5 vertices, count pairs of vertices (u, v) such that their distance is >= D and the indu... |
