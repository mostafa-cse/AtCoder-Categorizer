# Backtracking

**Taxonomy Path**: `Miscellaneous` > `General` > `Backtracking`

## Description
This topic focuses on backtracking techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For columns $c_1$ and $c_2$ to pair symmetrically, their characters across all paired rows must be reverse complements of each other ($S[u][c_1] == S[v][c_2]$ and $S[v][c_1] == S[u][c_2]$). Column signatures allow greedy matching in $O(W^2)$ time per row pairing.
- Common Reductions: Determine if swapping rows and columns can make an $H \times W$ grid ($H, W \le 12$) symmetric under 180-degree rotation. By transposing if necessary, assume $H \le W \le 12$. The $H$ rows must be partitioned into pairs $(u, v)$ (and at most one center row if $H$ is odd). There are at most $11!! = 10395$ such row pairings. For each fixed row pairing, check if the $W$ columns can be paired up to match symmetric signatures.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc095_c`](../../analysis/AtCoder-arc095_c.md) | E. Symmetric Grid | 2441 | Determine if swapping rows and columns can make an $H \times W$ grid ($H, W \le 12$) symmetric under 180-degree rotation... |
