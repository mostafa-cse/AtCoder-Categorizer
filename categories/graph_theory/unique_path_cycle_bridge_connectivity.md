# Articulation Bridges and Bridge Tree

**Taxonomy Path**: `Graph Theory` > `Graph Connectivity` > `Articulation Bridges and Bridge Tree`

## Description
This topic focuses on articulation bridges and bridge tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: All C_i = 0 pairs must lie on a tree of bridges, meaning they cannot belong to the same 2-edge-connected component. We merge vertices connected by C_i = 0 into tree components. If any C_i = 1 pair is merged into the same tree component with only tree edges, they have a unique path, creating a contradiction. Edge bounds on component count K decide feasibility.
- Common Reductions: Construct a connected simple graph with N vertices and M edges such that given pairs (A_i, B_i) have a unique simple path (C_i = 0) or multiple simple paths (C_i = 1). A pair has a unique simple path iff all edges on the path are bridges. All C_i = 0 constraints can be contracted via DSU into trees of bridges. C_i = 1 constraints require endpoints to belong to a cycle, which imposes bounds on available cross-edges and component sizes.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc038_d`](../../analysis/AtCoder-agc038_d.md) | Unique Path | 2682 | Construct a connected simple graph with N vertices and M edges such that given pairs (A_i, B_i) have a unique simple pat... |
