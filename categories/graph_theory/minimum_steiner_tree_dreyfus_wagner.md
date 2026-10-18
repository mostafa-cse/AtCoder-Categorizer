# Steiner Tree Problem

**Taxonomy Path**: `Graph Theory` > `Minimum Spanning Tree (MST)` > `Steiner Tree Problem`

## Description
This topic focuses on steiner tree problem techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Dreyfus-Wagner Minimum Steiner Tree DP on terminal subset $S \subseteq \{1 \dots K\}$. Precomputing extensions for each single query terminal $s \in [K, N-1]$ via $ndp_s[mask][u]$ allows every two-terminal query $(s, t)$ to be answered in $O(1)$ time by querying $ndp_s[(1 \ll K) - 1][t]$.
- Common Reductions: Given edge weights $C_{u, v}$ and $K \le 8$ fixed terminal vertices $\{1 \dots K\}$, answer $Q$ queries: find the minimum weight connected subgraph spanning $\{1 \dots K\} \cup \{s, t\}$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc395_g`](../../analysis/AtCoder-abc395_g.md) | G. Minimum Steiner Tree 2 | 2561 | Given edge weights $C_{u, v}$ and $K \le 8$ fixed terminal vertices $\{1 \dots K\}$, answer $Q$ queries: find the minimu... |
