# Interval DP / Range DP / Matrix Chain Multiplication (MCM)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Classic DP` > `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`

## Description
This topic focuses on interval dp / range dp / matrix chain multiplication (mcm) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Reverse the process: start with the target colors $C_i$ and repaint contiguous intervals to color 0. A final operation on interval $[l, r)$ costs $(r - l) + X_c$, where endpoints $l$ and $r-1$ must originally have color $c$. Operations form a non-crossing laminar family, reducing the problem to Interval DP. Unroll the circular cake into an array of length $2N$. Let $dp[l][r]$ be the minimum cost to clear $[l, r)$ to color 0, and $ep[l][r]$ be the minimum cost to make all elements in $[l, r)$ either color 0 or color $C_l$. For $m \in (l, r)$, transitions split via $dp[l][m] + dp[m][r]$ and $ep[l][m] + dp[m][r]$. When $C_l == C_{r-1}$, we transition $ep[l][r] = \min(ep[l][r], ep[l][r-1])$ and $dp[l][r] = \min(dp[l][r], ep[l][r] + (r - l) + X_{C_l})$. The answer is $\min_{0 \le i < N} dp[i][i + N]$.
- Common Reductions: A circular cake has $N$ equal slices ($N \le 400$). Slices initially have color 0 and must end with color $C_i \in [1, N]$. An operation paints $b$ contiguous slices starting at $a$ with color $c$ for cost $b + X_c$. Find the minimum total cost to reach the target configuration.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc400_f`](../../analysis/AtCoder-abc400_f.md) | F. Happy Birthday! 3 | 2263 | A circular cake has $N$ equal slices ($N \le 400$). Slices initially have color 0 and must end with color $C_i \in [1, N... |
