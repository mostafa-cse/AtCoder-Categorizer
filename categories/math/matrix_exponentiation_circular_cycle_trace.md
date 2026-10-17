# Matrix Exponentiation

**Taxonomy Path**: `Math` > `Matrices` > `Matrix Exponentiation`

## Description
This topic focuses on matrix exponentiation techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Notice that if we fix the total number of black stones on every edge to be some constant $k \in [0, D+1]$, then for an edge $(u, v)$ where vertex $u$ has stone color $x \in \{0, 1\}$ and vertex $v$ has stone color $y \in \{0, 1\}$, the remaining $k - x - y$ black stones must be placed among the $D-1$ inner stones on that edge. The number of ways to choose them is $\binom{D-1}{k - x - y}$.
This defines a $2 \times 2$ transition matrix $M_k$ between vertex stone colors. Because the vertices form an $N$-cycle, the number of valid assignments for a fixed $k$ is precisely the trace $\text{Tr}(M_k^N) = (M_k^N)_{0,0} + (M_k^N)_{1,1}$. Summing this over all $k \in [0, D+1]$ gives the total answer.
- Common Reductions: We are given a cycle of $N$ edges and $N$ vertices. On each edge $i$, we choose white or black stones such that the total number of black stones on the edge is between $0$ and $D+1$, including the two stones placed at its incident vertices. Each edge has $D-1$ inner stones, and we want to count the number of valid stone assignments modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc256_g`](../../analysis/AtCoder-abc256_g.md) | G. Black and White Stones | 2250 | We are given a cycle of $N$ edges and $N$ vertices. On each edge $i$, we choose white or black stones such that the tota... |
