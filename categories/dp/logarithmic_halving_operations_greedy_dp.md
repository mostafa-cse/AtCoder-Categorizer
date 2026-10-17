# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because each Takahashi operation halves the maximum height, Takahashi can perform at most $\approx 32$ operations even if Aoki pulls 0 weeds. Sort $A$ ascending. For weed $i$, Takahashi's operation eliminates all weeds in $(prev[i], i]$ where $A_{prev[i]} \le \lfloor A_i / 2 \rfloor$.
Let $DP[i][j]$ be the minimum Aoki pulls to clear prefix $1 \dots i$ using at most $j$ Takahashi operations. Transitions: Aoki pulls weed $i$ ($DP[i][j] = DP[i-1][j] + 1$), or Takahashi operates on weed $i$ ($DP[i][j] = \min(DP[i][j], DP[prev[i]][j-1])$).
- Common Reductions: Given $N$ weeds with heights $A_1, \dots, A_N$. Aoki can pull at most $K$ weeds. Then Takahashi repeatedly pulls all weeds with height $> H / 2$ where $H$ is the maximum remaining weed height. Aoki wants to minimize Takahashi's operations, and then minimize Aoki's pulls.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc203_f`](../../analysis/AtCoder-abc203_f.md) | F. Weed | 2252 | Given $N$ weeds with heights $A_1, \dots, A_N$. Aoki can pull at most $K$ weeds. Then Takahashi repeatedly pulls all wee... |
