# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If the $K$-th largest cell value on the optimal path is $X = A_{r, c}$, then every cell with $A_{i, j} > X$ must be counted, cells with $A_{i, j} < X$ cannot be counted, and cells with $A_{i, j} = X$ can optionally be counted to reach exactly $K$ selections.
- Common Reductions: In an $H \times W$ grid with values $A_{i, j}$, find the minimum sum of the $K$ largest elements along any shortest path from $(1, 1)$ to $(H, W)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc227_f`](../../analysis/AtCoder-abc227_f.md) | I. Treasure Hunting | 2323 | In an $H \times W$ grid with values $A_{i, j}$, find the minimum sum of the $K$ largest elements along any shortest path... |
