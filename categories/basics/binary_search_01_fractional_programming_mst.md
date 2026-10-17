# Binary Search

**Taxonomy Path**: `Basics` > `Leveraging Monotonicity` > `Binary Search`

## Description
This topic focuses on binary search techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In 0-1 fractional programming minimizing $\frac{\sum C_e}{\sum T_e} \le \lambda$, the objective is equivalent to determining whether there exists a connected spanning subgraph such that $\sum (C_e - \lambda T_e) \le 0$. Since we may include extra edges with $C_e - \lambda T_e < 0$, the optimal edge selection takes an MST on transformed weights $w_e = C_e - \lambda T_e$, plus all remaining negative edges.
- Common Reductions: Given a connected undirected multigraph with edge costs $C_i$ and construction times $T_i$, find a connected spanning subgraph that minimizes the overall cost-to-time ratio $\frac{\sum C_e}{\sum T_e}$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc026_4`](../../analysis/AtCoder-arc026_4.md) | D. Highway Construction | 2297 | Given a connected undirected multigraph with edge costs $C_i$ and construction times $T_i$, find a connected spanning su... |
