# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: After sorting by $H_i + P_i$, let $DP[j]$ be the minimum total cushions stacked by a subset of $j$ participants. For each participant $(H_i, P_i)$, if $DP[j] \le H_i$, transition $DP[j + 1] = \min(DP[j + 1], DP[j] + P_i)$ in reverse order.
- Common Reductions: Maximize participants who can stack cushions. Participant $i$ can stack $P_i$ cushions if the current stack has at most $H_i$ cushions. By exchange argument, consider participants $i$ and $j$ stacked adjacent. For both to succeed in order $(i, j)$, initial stack $S \le \min(H_i, H_j - P_i)$. Swapping to $(j, i)$ requires $S \le \min(H_j, H_i - P_j)$. Order $(i, j)$ is weakly superior if $H_j - P_i \ge H_i - P_j \iff H_i + P_i \le H_j + P_j$. Sorting participants by $H_i + P_i$ ascending establishes the canonical order, after which a 1D Knapsack DP computes the maximum count.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-cf17_final_d`](../../analysis/AtCoder-cf17_final_d.md) | D. Zabuton | 2509 | Maximize participants who can stack cushions. Participant $i$ can stack $P_i$ cushions if the current stack has at most ... |
