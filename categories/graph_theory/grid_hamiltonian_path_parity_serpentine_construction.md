# Hamiltonian Path and Cycle

**Taxonomy Path**: `Graph Theory` > `Hamiltonian Path` > `Hamiltonian Path and Cycle`

## Description
This topic focuses on hamiltonian path and cycle techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In an $N \times N$ grid, start $(1, 1)$ and end $(N, N)$ have identical bipartite colors iff $N$ is odd, so even $N$ has no Hamiltonian path. Net horizontal displacement requires $R - L = N - 1$, and parity matching restricts $K$ to even values in $[N - 1, (N^2 - 1)/2]$, realized via serpentine column-loop folding.
- Common Reductions: Construct an $N \times N$ matrix filled with integers from 1 to $N^2$ such that each row and each column contains exactly $K$ adjacent pairs whose difference is 1 in absolute value, or report impossible.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc474_g`](../../analysis/AtCoder-abc474_g.md) | G. LRUD Moving 2 | 2280 | Construct an $N \times N$ matrix filled with integers from 1 to $N^2$ such that each row and each column contains exactl... |
