# Generating Functions

**Taxonomy Path**: `Math` > `Polynomial` > `Generating Functions`

## Description
This topic focuses on generating functions techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Total operations satisfy $\sum_{j=1}^{N - K + 1} x_j + \sum_{i=1}^N y_i = M / K$, with $0 \le x_j < K$ and $y_i \ge 0$. The number of ways to choose non-negative integers is given by the coefficient of $t^{M/K}$ in the generating function $\frac{(1 - t^K)^{N - K + 1}}{(1 - t)^{2N - K + 1}}$, extracted in $O(N)$ time via binomial expansion.
- Common Reductions: Count sequences $A_1, \dots, A_N$ reachable from all zeros by two operations: adding $K$ to a single element $A_i$ (Op 1), or adding 1 to a contiguous subsegment of length $K$ (Op 2), such that $\sum A_i = M$. An operation of adding $K$ to the same contiguous subsegment of length $K$ is equivalent to performing Op 1 on each element in that segment. Thus, a canonical representation restricts Op 2 on any subsegment to be applied at most $K - 1$ times. The remaining operations are Op 1 on individual elements.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc160_d`](../../analysis/AtCoder-arc160_d.md) | D. Mahjong | 2485 | Count sequences $A_1, \dots, A_N$ reachable from all zeros by two operations: adding $K$ to a single element $A_i$ (Op 1... |
