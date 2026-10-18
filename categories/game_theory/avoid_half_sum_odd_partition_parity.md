# Grundy Number and Basic Game Theory

**Taxonomy Path**: `Game Theory` > `Grundy Number / Nim` > `Grundy Number and Basic Game Theory`

## Description
This topic focuses on grundy number and basic game theory techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Choosing $X_i \in \{B_i, C_i\}$ is equivalent to choosing $X_i \in \{0, D_i\}$ where $D_i = |B_i - C_i| \le A_i$ with $D_i \equiv A_i \pmod 2$. A half-sum subset is unavoidable if and only if every possible choice of $D$ can represent $S/2$. By induction, the necessary and sufficient condition for the existence of such avoiding $D$ is that there exists some index $i$ such that the number of odd integers among $A_1, \dots, A_N$ strictly less than $A_i$ is strictly less than $A_i - 1$.
- Common Reductions: Determine whether there exists a decomposition $B_i + C_i = A_i$ such that no subset choice of $B_i$ or $C_i$ totals half the total sum $S/2$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc065_c`](../../analysis/AtCoder-agc065_c.md) | C - Avoid Half Sum | 2414 | Determine whether there exists a decomposition $B_i + C_i = A_i$ such that no subset choice of $B_i$ or $C_i$ totals hal... |
