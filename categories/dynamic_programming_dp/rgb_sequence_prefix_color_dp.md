# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Due to symmetry of color names, the state only needs to track $(i, j, k)$ with $k < j < i$: the current prefix length $i$, the last position $j$ of the second most recent color, and the last position $k$ of the third most recent color. The number of distinct colors in interval $[L, i]$ is simply $1 + [j \ge L] + [k \ge L]$. All constraints ending at $R = i$ can be checked immediately against this formula.
- Common Reductions: We have $N$ positions colored with 3 colors (Red, Green, Blue). There are $M$ constraints: interval $[L_i, R_i]$ must contain exactly $X_i$ distinct colors. Formulate a DP state that tracks the positions of the most recent occurrences of the three colors. When moving from step $i - 1$ to $i$, the new position $i$ takes one color, and the other two colors last appeared at positions $j$ and $k$ with $0 \le k < j < i$ (where 0 indicates the color hasn't appeared yet).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc074_c`](../../analysis/AtCoder-arc074_c.md) | E. RGB Sequence | 2519 | We have $N$ positions colored with 3 colors (Red, Green, Blue). There are $M$ constraints: interval $[L_i, R_i]$ must co... |
