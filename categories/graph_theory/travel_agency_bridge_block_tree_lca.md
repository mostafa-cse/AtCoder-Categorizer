# Articulation Bridges and Bridge Tree

**Taxonomy Path**: `Graph Theory` > `Graph Connectivity` > `Articulation Bridges and Bridge Tree`

## Description
This topic focuses on articulation bridges and bridge tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In the Bridge Block Tree, component $comp[B]$ lies on the simple tree path between $comp[A]$ and $comp[C]$ if and only if $\text{dist}(comp[A], comp[B]) + \text{dist}(comp[B], comp[C]) == \text{dist}(comp[A], comp[C])$. Tree distances are computed in $O(\log N)$ using binary lifting and LCA.
- Common Reductions: Given an undirected connected graph, answer $Q$ queries: does there exist a trail (no repeated edges) from $A$ to $C$ passing through $B$? Contract all 2-edge-connected components (2-ECCs) by finding bridges using Tarjan's algorithm to construct the Bridge Block Tree. In any 2-ECC, any two vertices have two edge-disjoint paths between them. Thus, a valid trail exists if and only if $B$'s component lies on the tree path between $A$'s component and $C$'s component.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc039_d`](../../analysis/AtCoder-arc039_d.md) | D. 旅行会社高橋君 | 2550 | Given an undirected connected graph, answer $Q$ queries: does there exist a trail (no repeated edges) from $A$ to $C$ pa... |
