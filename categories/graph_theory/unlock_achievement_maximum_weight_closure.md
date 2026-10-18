# Maximum Closure Problem

**Taxonomy Path**: `Graph Theory` > `Flow and Min Cut` > `Maximum Closure Problem`

## Description
This topic focuses on maximum closure problem techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because skill levels are bounded by 5, there are at most $4N \le 200$ skill upgrade steps. Each upgrade is a prerequisite for subsequent levels. The closed subgraph selection guarantees that selecting an achievement forces all required skill level upgrades, which is solved by standard project selection reduction.
- Common Reductions: Maximize net profit: achievement rewards minus skill upgrade costs. Model as Maximum Weight Closure on a directed DAG via Minimum Cut. Each achievement gives positive reward $A_i$ and depends on skill level nodes $(j, L_{i, j})$. Upgrading skill $j$ from level $l-1$ to $l$ incurs cost $C_j$, with level $(j, l)$ depending on level $(j, l-1)$. Dinic's algorithm computes the minimum cut.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc326_g`](../../analysis/AtCoder-abc326_g.md) | G. Unlock Achievement | 2470 | Maximize net profit: achievement rewards minus skill upgrade costs. Model as Maximum Weight Closure on a directed DAG vi... |
