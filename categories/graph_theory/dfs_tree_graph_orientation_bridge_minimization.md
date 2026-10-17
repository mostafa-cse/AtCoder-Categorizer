# DFS Tree

**Taxonomy Path**: `Graph Theory` > `Graph Traversal` > `DFS Tree`

## Description
This topic focuses on dfs tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Contracting pillar edges (j, j+N) yields a multigraph of N vertices and M edges. Directed cycles in the contracted graph lift to undirected cycles in the 2N graph using vertical edges. By Robbins' Theorem and DFS tree properties, directing tree edges forward (parent to child) and back edges backward (descendant to ancestor) strongly connects every 2-edge-connected component, eliminating all non-trivial bridges.
- Common Reductions: Orient M edges between top and bottom vertices in a 2N-vertex graph with fixed pillar edges (j, j+N) to minimize the number of bridges.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc143_d`](../../analysis/AtCoder-arc143_d.md) | Bridges | 2229 | Orient M edges between top and bottom vertices in a 2N-vertex graph with fixed pillar edges (j, j+N) to minimize the num... |
