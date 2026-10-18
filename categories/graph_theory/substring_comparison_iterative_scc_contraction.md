# Strongly Connected Components (SCC)

**Taxonomy Path**: `Graph Theory` > `Graph Connectivity` > `Strongly Connected Components (SCC)`

## Description
This topic focuses on strongly connected components (scc) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each constraint requires $X_{A_i} \le X_{C_i}$. Cycles of $\le$ relations enforce equality $X_u = X_v$ across SCC components. When $X_{A_i} = X_{C_i}$, the constraint advances to the next character $X[A_i+1, B_i] < X[C_i+1, D_i]$. If identical characters occur when both substrings end, a contradiction is reached.
- Common Reductions: Determine if there exists a sequence $X$ satisfying $M$ lexicographical constraints $X[A_i, B_i] < X[C_i, D_i]$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc165_d`](../../analysis/AtCoder-arc165_d.md) | D. Substring Comparison | 2589 | Determine if there exists a sequence $X$ satisfying $M$ lexicographical constraints $X[A_i, B_i] < X[C_i, D_i]$.... |
