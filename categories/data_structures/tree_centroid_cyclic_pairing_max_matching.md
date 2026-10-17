# Centroid Decomposition

**Taxonomy Path**: `Data Structures (DS)` > `Centroid Decomposition` > `Centroid Decomposition`

## Description
This topic focuses on centroid decomposition techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Root the tree at its centroid C. Every branch attached to C has size at most floor(N/2). In a DFS traversal order of vertices starting from C, offsetting by floor(N/2) places the partner of any vertex in a completely different branch (or at C). Thus, every pair (v_i, v_{i + floor(N/2)}) has its tree path passing through C, saturating every tree edge to its maximum possible crossing capacity.
- Common Reductions: In a complete graph whose edge weights are tree shortest path distances, construct a maximum weight matching of floor(N/2) pairs. The theoretical upper bound sum_e min(sz_e, N - sz_e) is achieved when all matched pairs cross the tree centroid.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc362_f`](../../analysis/AtCoder-abc362_f.md) | I. Perfect Matching on a Tree | 2186 | In a complete graph whose edge weights are tree shortest path distances, construct a maximum weight matching of floor(N/... |
