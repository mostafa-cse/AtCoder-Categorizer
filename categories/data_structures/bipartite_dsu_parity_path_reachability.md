# Augmented DSU / Weighted DSU

**Taxonomy Path**: `Data Structures (DS)` > `Disjoint Set Union (DSU)` > `Augmented DSU / Weighted DSU`

## Description
This topic focuses on augmented dsu / weighted dsu techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because backtracking along an edge adds an even distance (2 * z), any path parity can be adjusted by traversing an odd cycle. If two nodes are in a component with an odd cycle, both even and odd walks exist. If the component is bipartite, only paths with parity matching the 2-coloring exist. Doubling the graph nodes into 2N vertices (u: even, u+N: odd) seamlessly tracks component parity and odd cycles.
- Common Reductions: Process edge additions and queries asking if two cities can be connected by an even-length walk in a dynamic undirected graph.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc036_d`](../../analysis/AtCoder-arc036_d.md) | 偶数メートル | 2227 | Process edge additions and queries asking if two cities can be connected by an even-length walk in a dynamic undirected ... |
