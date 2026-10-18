# Hamiltonian Path and Cycle

**Taxonomy Path**: `Graph Theory` > `Hamiltonian Path` > `Hamiltonian Path and Cycle`

## Description
This topic focuses on hamiltonian path and cycle techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If we choose all $A$ values, the cycle cost is $\sum A_i$. If all $B$, cost is $\sum B_i$. Otherwise, as long as there is at least one vertex with both $A_i$ and $B_i$ chosen, the edges can always be configured into a single Eulerian component that forms a Hamiltonian cycle. Sorting all $2N$ values allows finding the minimal cost choice in $O(N \log N)$.
- Common Reductions: Find a Hamiltonian cycle on a complete directed graph where edge $(u, v)$ has cost $\min(A_u, B_v)$. In any Hamiltonian cycle, each vertex $i$ has in-degree 1 and out-degree 1, selecting $N$ values from $\{A_i\} \cup \{B_i\}$. A set of $N$ chosen values can form a single connected cycle iff the set is all $A$, all $B$, or contains both $A_i$ and $B_i$ for at least one vertex $i$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc028_c`](../../analysis/AtCoder-agc028_c.md) | C. Min Cost Cycle | 2463 | Find a Hamiltonian cycle on a complete directed graph where edge $(u, v)$ has cost $\min(A_u, B_v)$. In any Hamiltonian ... |
