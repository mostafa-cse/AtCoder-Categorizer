# Reachability Tree / DSU Tree / Kruskal Reconstruction Tree (KRT)

**Taxonomy Path**: `Data Structures (DS)` > `Disjoint Set Union (DSU)` > `Reachability Tree / DSU Tree / Kruskal Reconstruction Tree (KRT)`

## Description
This topic focuses on reachability tree / dsu tree / kruskal reconstruction tree (krt) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Reachability subsets using edges of weight <= w are precisely the subtrees in the Kruskal Reconstruction Tree (KRT). Multiple edges of the same weight merge multiple components simultaneously. Each KRT node represents a connected component at weight w. Choosing to paint a component adds all its leaves. A tree DP computes the generating polynomial P_u(X) = sum c_k X^k where c_k is the number of painted subsets of size k. When components merge, the new valid sets are prod_c P_c(X) - X^m + X, truncated to degree K.
- Common Reductions: In a connected undirected weighted graph with N vertices, M edges, and parameter K <= 300, count the number of reachable vertex subsets of size <= K formed by threshold reachability components, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc235_h`](../../analysis/AtCoder-abc235_h.md) | Ex - Painting Weighted Graph | 2966 | In a connected undirected weighted graph with N vertices, M edges, and parameter K <= 300, count the number of reachable... |
