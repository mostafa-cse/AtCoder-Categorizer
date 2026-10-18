# System Of Difference Constraints

**Taxonomy Path**: `Graph Theory` > `Satisfiability` > `System Of Difference Constraints`

## Description
This topic focuses on system of difference constraints techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: To make $S$ lexicographically smallest, we greedily want $S[i-1] = '0'$ wherever possible, which corresponds to setting $dist[i]$ larger than $dist[i-1]$. In 0-1 BFS starting from vertex 0, the shortest path distance represents the minimum potential satisfying the distance metric. Since adjacent vertices differ by at most 1, $dist[i] > dist[i-1]$ implies character '0', and $dist[i] < dist[i-1]$ implies character '1'.
- Common Reductions: Find the lexicographically smallest 01 string $S$ of length $N$ such that each given substring $S[L_i \dots R_i]$ has an equal number of 0s and 1s. Let $dist[i]$ be the prefix difference (count of 1s minus count of 0s in $S[0 \dots i-1]$). Each step changes $dist$ by $\pm 1$: $|dist[i] - dist[i-1]| \le 1$. Equal 0s and 1s in $[L_i, R_i]$ means $dist[R_i] = dist[L_i - 1]$. Model as a system of difference constraints and shortest path on a parity-preserving graph with 0-weight edges for range constraints and 1-weight edges for adjacent prefix steps. 0-1 BFS finds potentials, determining $S[i-1] = '0'$ if $dist[i] > dist[i-1]$ else $'1'$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc056_c`](../../analysis/AtCoder-agc056_c.md) | C. 01 Balanced | 2481 | Find the lexicographically smallest 01 string $S$ of length $N$ such that each given substring $S[L_i \dots R_i]$ has an... |
