# Binary Lifting and LCA

**Taxonomy Path**: `Graph Theory` > `Lowest Common Ancestor (LCA)` > `Binary Lifting and LCA`

## Description
This topic focuses on binary lifting and lca techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The condition dist(u, w) <= dist(v, w) partitions the tree into two connected components along the midpoint of the path between u and v. Using binary lifting and LCA, we can find the midpoint on the u-v path in O(log N) time. The tree is thus split into two subtrees: u's side and v's side. With tree rerooting DP, we can precompute sum of distances from every vertex to all other vertices. For each query, the sum of distances restricted to each side can be computed in O(log N) using precomputed subtree aggregates.
- Common Reductions: Given a tree of N vertices, answer Q queries: given two vertices u and v, compute sum_{w=1}^N min(dist(u, w), dist(v, w)).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc298_h`](../../analysis/AtCoder-abc298_h.md) | Ex - Sum of Min of Length | 2792 | Given a tree of N vertices, answer Q queries: given two vertices u and v, compute sum_{w=1}^N min(dist(u, w), dist(v, w)... |
