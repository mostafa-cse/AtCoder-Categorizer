# Interval DP / Range DP / Matrix Chain Multiplication (MCM)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Classic DP` > `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`

## Description
This topic focuses on interval dp / range dp / matrix chain multiplication (mcm) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: State $DP[l][r][k]$ is the maximum tastiness Snuke gets from remaining candies outside $[l, r]$ given $k$ available turns. Snuke can spend 1 turn to take $a_{l-1}$ or $a_{r+1}$, or let Ant move (Ant takes $\max(a_{l-1}, a_{r+1})$ and Snuke receives $+1$ turn). The DP table is independent of $p$! Computing the table once answers all $p$ via $DP[p + 1][p][1]$ in $O(N^3)$ total time.
- Common Reductions: There are $N$ candies $a_1 \dots a_N$. Ant starts between candies $p$ and $p + 1$. Snuke and Ant alternate turns. Snuke can pick any candy. Ant greedily picks $\max(a_{l-1}, a_{r+1})$ adjacent to the eaten range $[l, r]$. Find Snuke's maximum score for each starting position $p \in [0, N]$. Ant's eaten candies always form a contiguous interval $[l, r]$. Model as Interval DP where $k$ is the number of tokens (unclaimed turns) Snuke holds.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-keyence2021_e`](../../analysis/AtCoder-keyence2021_e.md) | E. Greedy Ant | 2560 | There are $N$ candies $a_1 \dots a_N$. Ant starts between candies $p$ and $p + 1$. Snuke and Ant alternate turns. Snuke ... |
