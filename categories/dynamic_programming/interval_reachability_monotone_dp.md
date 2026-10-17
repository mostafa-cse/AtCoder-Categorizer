# 1D1D DP Optimization

**Taxonomy Path**: `Dynamic Programming (DP)` > `DP Optimizations` > `1D1D DP Optimization`

## Description
This topic focuses on 1d1d dp optimization techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Adding sentinels at 1, 2 and $N+3, N+4$ models full traversals. For each target index $z$, a valid previous position $y$ must satisfy $A_z \le y < B_z$ where $A_z = \max_{R_j < z} L_j$ and $B_z = \min_{z \le R_j} L_j$. The set of reachable earlier positions at each step forms a contiguous interval $[L_{dp}[z], R_{dp}[z]]$ due to monotonicity of $A_z$ and $B_z$.
- Common Reductions: Given intervals $[L_j, R_j]$, find whether there exists a permutation visiting elements such that consecutive steps adhere to interval constraints. Adding sentinels and tracking valid predecessor ranges via 1D monotone reachability DP solves in $O((N + M) \log N)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc232_a`](../../analysis/AtCoder-arc232_a.md) | A. Permutation Journey | 2331 | Given intervals $[L_j, R_j]$, find whether there exists a permutation visiting elements such that consecutive steps adhe... |
