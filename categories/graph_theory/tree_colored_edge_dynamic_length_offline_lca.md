# Binary Lifting and LCA

**Taxonomy Path**: `Graph Theory` > `Lowest Common Ancestor (LCA)` > `Binary Lifting and LCA`

## Description
This topic focuses on binary lifting and lca techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The distance between $u$ and $v$ when edges of color $x$ are set to length $y$ is $\text{dist}(u, v) - \text{sum}(u, v, x) + \text{cnt}(u, v, x) \cdot y$, where $\text{cnt}(u, v, x)$ and $\text{sum}(u, v, x)$ decompose along the tree path via $u + v - 2 \cdot \text{lca}(u, v)$.
- Common Reductions: Given a tree with colored weighted edges, answer $Q$ queries: if all edges of color $x$ have their weights replaced with $y$, what is the distance between vertices $u$ and $v$?

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc133_f`](../../analysis/AtCoder-abc133_f.md) | F. Colorful Tree | 2330 | Given a tree with colored weighted edges, answer $Q$ queries: if all edges of color $x$ have their weights replaced with... |
