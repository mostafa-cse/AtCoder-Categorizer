# Linear Programming / Simplex Algorithm

**Taxonomy Path**: `Math` > `Mathematical Optimization` > `Linear Programming / Simplex Algorithm`

## Description
This topic focuses on linear programming / simplex algorithm techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each item $i$ can produce resource rates $u_i = A_i / C_i$ and $v_i = B_i / C_i$ per unit cost. We want to choose convex combinations of points $(u_i, v_i)$ in the 2D plane to maximize $\min(u, v)$. The optimal point is either an individual vertex $(u_i, v_i)$ (giving $\min(u_i, v_i)$), or the intersection of a segment between two hull vertices with the line $u = v$.
- Common Reductions: Given items with values $A_i, B_i$ and costs $C_i$, find $\lim_{X \to \infty} f(X) / X$, where $f(X)$ is the minimum cost to achieve at least $X$ of both resources $A$ and $B$. In the asymptotic limit, this is a continuous linear program: minimize $\sum x_i C_i$ subject to $\sum x_i A_i \ge 1, \sum x_i B_i \ge 1, x_i \ge 0$. By duality, this is equivalent to finding the maximum of $\min(u, v)$ on the lower-left boundary of the convex hull of points $(C_i / A_i, C_i / B_i)$, or equivalently minimizing $\max(u, v)$ in the dual space.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc275_g`](../../analysis/AtCoder-abc275_g.md) | G. Infinite Knapsack | 2522 | Given items with values $A_i, B_i$ and costs $C_i$, find $\lim_{X \to \infty} f(X) / X$, where $f(X)$ is the minimum cos... |
