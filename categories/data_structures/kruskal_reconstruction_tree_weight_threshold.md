# Reachability Tree / DSU Tree / Kruskal Reconstruction Tree (KRT)

**Taxonomy Path**: `Data Structures (DS)` > `Disjoint Set Union (DSU)` > `Reachability Tree / DSU Tree / Kruskal Reconstruction Tree (KRT)`

## Description
This topic focuses on reachability tree / dsu tree / kruskal reconstruction tree (krt) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In the Kruskal Reconstruction Tree ordered by edge weight $Y_e$, a subtree $u$ represents a connected component formed by all edges of weight $\le \mathrm{val}[u]$. The component is valid if total vertex weight $W(u) \ge \mathrm{val}[u]$. If valid, all edges inside subtree $u$ are preserved without deletion.
- Common Reductions: Given a weighted graph with vertex weights $X_v$ and edge weights $Y_e$, find the minimum number of edges to delete such that every remaining edge belongs to a connected component whose total vertex weight is at least its edge weight.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-nikkei2019_qual_e`](../../analysis/AtCoder-nikkei2019_qual_e.md) | E. Avoid Deletion | 2294 | Given a weighted graph with vertex weights $X_v$ and edge weights $Y_e$, find the minimum number of edges to delete such... |
