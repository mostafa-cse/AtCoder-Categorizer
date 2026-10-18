# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: When deleting exactly $K$ balls such that adjacent remaining balls have distinct colors, the optimal value for each deletion count $j \in [0, K]$ depends only on the color of the last kept ball. Because a new ball of color $C_i$ can transition from any previous state with color $\ne C_i$, it suffices to maintain only the top 2 maximum values with distinct colors for each deletion count $j$.
- Common Reductions: Delete exactly $K$ balls such that adjacent remaining balls have distinct colors, maximizing total value. For each deletion count $j \le K$, maintaining only the top 2 maximum values with distinct colors allows $O(1)$ transitions per ball in $O(NK)$ time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc345_e`](../../analysis/AtCoder-abc345_e.md) | E. Colorful Subsequence | 2356 | Delete exactly $K$ balls such that adjacent remaining balls have distinct colors, maximizing total value. For each delet... |
