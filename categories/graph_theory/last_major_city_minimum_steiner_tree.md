# Steiner Tree Problem

**Taxonomy Path**: `Graph Theory` > `Minimum Spanning Tree (MST)` > `Steiner Tree Problem`

## Description
This topic focuses on steiner tree problem techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because $K - 1 \le 9$, the number of terminal masks is at most $2^9 = 512$. For each mask, we perform submask splitting $dp[mask][v] = \min_{sub} (dp[sub][v] + dp[mask \setminus sub][v])$ followed by Dijkstra edge relaxation across the entire graph.
- Common Reductions: Given a graph with $N \le 4000$ cities and $M \le 8000$ edges, cities $1 \dots K-1$ ($K \le 10$) are fixed major cities. For each city $i \in [K, N]$, find the minimum cost of a tree connecting $1 \dots K-1$ and $i$. This is solved by the Dreyfus-Wagner Minimum Steiner Tree algorithm on terminal set $T = \{1, \dots, K-1\}$, where $dp[mask][v]$ represents the minimum tree connecting $mask \subseteq T$ rooted at vertex $v$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc364_g`](../../analysis/AtCoder-abc364_g.md) | G. Last Major City | 2455 | Given a graph with $N \le 4000$ cities and $M \le 8000$ edges, cities $1 \dots K-1$ ($K \le 10$) are fixed major cities.... |
