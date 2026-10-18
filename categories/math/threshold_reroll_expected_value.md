# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: From any state $X$, the decision to reroll or increment depends only on distance $T - X$. If $X > T$, rerolling is mandatory. If $X < T$, the optimal policy increments if $T - X \le k$ and rerolls otherwise, leading to expected reroll cost $E(k) = \frac{NB}{k+1} + \frac{Ak}{2}$, which is strictly convex in threshold $k$.
- Common Reductions: Find the minimum expected cost to reach target $T$ on an $N$-sided die with increment cost $A$ and reroll cost $B$. Optimal stopping strategy rerolls iff distance to $T$ exceeds threshold $k$; the expected cost $E(k) = \frac{NB}{k+1} + \frac{Ak}{2}$ is minimized via convex optimization in $O(1)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc224_g`](../../analysis/AtCoder-abc224_g.md) | G. Roll or Increment | 2374 | Find the minimum expected cost to reach target $T$ on an $N$-sided die with increment cost $A$ and reroll cost $B$. Opti... |
