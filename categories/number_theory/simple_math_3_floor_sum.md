# Floor Sum and Mod Sum of Arithmetic Progression

**Taxonomy Path**: `Number Theory` > `Floor Sum` > `Floor Sum and Mod Sum of Arithmetic Progression`

## Description
This topic focuses on floor sum and mod sum of arithmetic progression techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because the interval $[A + B i, A + C i]$ contains at most one multiple of $D$ for each $1 \le i \le M$, the total number of violating $i$ is exactly $\sum_{i=1}^M (\lfloor \frac{C i + A}{D} \rfloor - \lfloor \frac{B i + A - 1}{D} \rfloor)$. Since $A < D$ and $A \ge 1$, the terms at $i = 0$ are both 0. Thus the sum equals $\text{floor\_sum}(M + 1, D, C, A) - \text{floor\_sum}(M + 1, D, B, A - 1)$.
- Common Reductions: Given $A, B, C, D$, find the number of positive integers $i \ge 1$ such that the interval $[A + B i, A + C i]$ contains no multiple of $D$. Notice that if $(C - B) i \ge D$, the interval length is at least $D$, guaranteeing a multiple of $D$. Thus $i \le M = \lfloor (D - 1) / (C - B) \rfloor$. For $1 \le i \le M$, the interval has length $< D$, so it contains at most one multiple of $D$. The condition is violated if and only if $\lfloor (A + C i) / D \rfloor > \lfloor (A + B i - 1) / D \rfloor$, which is solved in $O(\log D)$ using floor_sum.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc111_e`](../../analysis/AtCoder-arc111_e.md) | E. Simple Math 3 | 2541 | Given $A, B, C, D$, find the number of positive integers $i \ge 1$ such that the interval $[A + B i, A + C i]$ contains ... |
