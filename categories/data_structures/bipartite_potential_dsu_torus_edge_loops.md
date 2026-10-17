# Augmented DSU / Weighted DSU

**Taxonomy Path**: `Data Structures (DS)` > `Disjoint Set Union (DSU)` > `Augmented DSU / Weighted DSU`

## Description
This topic focuses on augmented dsu / weighted dsu techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each edge presence on the grid is boolean. For each row, horizontal edge presences propagate by toggling on Type A tiles, requiring an even number of Type A tiles per row (and per column) to close around the torus. Type B tiles impose XOR relations between row and column edge variables, forming a bipartite graph of constraints. If any cycle is contradictory (odd parity), answer is 0; otherwise 2^{components}.
- Common Reductions: Determine the number of tile rotations of Type A (connecting adjacent edges) and Type B (connecting opposite edges) on an H x W torus grid such that line segments form closed loops without dead ends modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc196_b`](../../analysis/AtCoder-arc196_b.md) | B. Torus Loop | 2188 | Determine the number of tile rotations of Type A (connecting adjacent edges) and Type B (connecting opposite edges) on a... |
