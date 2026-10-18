# Reachability Tree / DSU Tree / Kruskal Reconstruction Tree (KRT)

**Taxonomy Path**: `Data Structures (DS)` > `Disjoint Set Union (DSU)` > `Reachability Tree / DSU Tree / Kruskal Reconstruction Tree (KRT)`

## Description
This topic focuses on reachability tree / dsu tree / kruskal reconstruction tree (krt) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The number of reachable vertices is monotonically non-decreasing with respect to $w$. Thus, we can binary search for the minimum $w \in [1, M]$ for each query. Parallel Binary Search maintains the search intervals $[L_q, R_q]$ for all queries simultaneously. In each of $\lceil \log_2 M \rceil$ rounds, edges $1 \dots M$ are added to a DSU, and queries with midpoint $mid = (L_q + R_q) / 2$ are checked in $O(1)$ time.
- Common Reductions: Given an undirected graph of $N$ vertices and $M$ edges with weights $1 \dots M$, answer $Q$ queries: find the minimum edge weight $w$ such that at least $z$ distinct vertices can be visited starting from $x$ and $y$ using only edges with weight $\le w$. Using edges $\le w$, the set of reachable vertices is the union of the connected components of $x$ and $y$, containing $sz(find(x)) + sz(find(y)) - [find(x) == find(y)] sz(find(x))$ vertices.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc002_d`](../../analysis/AtCoder-agc002_d.md) | D. Stamp Rally | 2514 | Given an undirected graph of $N$ vertices and $M$ edges with weights $1 \dots M$, answer $Q$ queries: find the minimum e... |
