# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For adjacent trees $(i, i+1)$, cutting $i$ before $i+1$ pays $H_{i+1}$, whereas cutting $i+1$ before $i$ pays $H_i$. Minimizing total cost imposes strict relative order constraints on adjacent cutting positions.
- Common Reductions: In a line of $N$ trees with heights $H_i$, cutting tree $P_i$ costs $H_{P_i-1} + H_{P_i} + H_{P_i+1}$. Count permutations minimizing the total cost, modulo $10^9+7$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc209_f`](../../analysis/AtCoder-abc209_f.md) | F. Deforestation | 2307 | In a line of $N$ trees with heights $H_i$, cutting tree $P_i$ costs $H_{P_i-1} + H_{P_i} + H_{P_i+1}$. Count permutation... |
