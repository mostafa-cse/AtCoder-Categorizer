# Bitmask DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Bit Related DP` > `Bitmask DP`

## Description
This topic focuses on bitmask dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any optimal railway line passes directly through at least one town ($x = X_i$ or $y = Y_i$). Moreover, among at most $N$ lines, each chosen line can be injectively associated with a distinct town. Hence, each town $i$ is assigned one of 3 states: (1) build vertical line $x = X_i$, (2) build horizontal line $y = Y_i$, or (0) build no line. There are $3^N = 3^{15} \approx 1.43 \times 10^7$ assignments. A ternary branch-and-bound DFS maintaining running distances for all $N$ towns evaluates all combinations in $\approx 140$ ms.
- Common Reductions: A grid city has initial railways along $x=0$ and $y=0$. There are $N \le 15$ towns with positions $(X_i, Y_i)$ and populations $P_i$. For each $K = 0, 1, \dots, N$, find the minimum weighted walking distance to railways if we build $K$ new horizontal or vertical railways.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-m_solutions2020_e`](../../analysis/AtCoder-m_solutions2020_e.md) | E. M's Solution | 2268 | A grid city has initial railways along $x=0$ and $y=0$. There are $N \le 15$ towns with positions $(X_i, Y_i)$ and popul... |
