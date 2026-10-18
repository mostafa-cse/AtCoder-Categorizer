# Contribution Technique

**Taxonomy Path**: `Combinatorics` > `Techniques` > `Contribution Technique`

## Description
This topic focuses on contribution technique techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In a bipartite directed tournament graph between $N$ row vertices and $N$ column vertices, an edge is uniquely determined iff it is not part of any directed alternating cycle. Therefore, the set of non-fixed entries corresponds to the union of non-trivial strongly connected components (SCCs) of size $(u_i, v_i)$ with $u_i \ge 2, v_i \ge 2$. Each such component contributes $u_i \times v_i$ non-fixed cells. The problem reduces to a 2D knapsack DP determining all achievable values of $\sum u_i v_i$ subject to $\sum u_i \le N$ and $\sum v_i \le N$.
- Common Reductions: Determine whether there exists an $N \times N$ grid of directed edges matching row/column constraints with exactly $K$ non-fixed entries.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc186_a`](../../analysis/AtCoder-arc186_a.md) | A - Underclued | 2511 | Determine whether there exists an $N \times N$ grid of directed edges matching row/column constraints with exactly $K$ n... |
