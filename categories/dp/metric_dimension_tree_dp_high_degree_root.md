# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Rooting at a vertex r of degree >= 3 guarantees that for every vertex u != r, the parent component already contains an antenna. Thus, for every node u, at most one child subtree can have 0 antennas. For leaf u, f(u) = 0. For internal node u with z children having f(v) = 0, f(u) = sum(f(v)) + max(0, z - 1). The answer is f(r).
- Common Reductions: Determine the minimum number of antennas required to uniquely identify any invaded vertex on a tree. Removing any vertex v with degree k must leave at least k - 1 connected components containing at least one antenna. If max degree <= 2, the tree is a path (answer 1). Otherwise, root the tree at any vertex of degree >= 3 and solve via simple bottom-up Tree DP.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-apc001_e`](../../analysis/AtCoder-apc001_e.md) | E. Antennas on Tree | 2167 | Determine the minimum number of antennas required to uniquely identify any invaded vertex on a tree. Removing any vertex... |
