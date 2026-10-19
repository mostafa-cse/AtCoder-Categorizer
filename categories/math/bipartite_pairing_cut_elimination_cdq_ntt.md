# Number Theoretic Transform (NTT)

**Taxonomy Path**: `Math` > `Convolution` > `Number Theoretic Transform (NTT)`

## Description
This topic focuses on number theoretic transform (ntt) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A directed graph is not strongly connected iff there exists a directed cut with no outgoing edges. Enumerating strongly connected components translates to subtracting disconnected configurations via a recurrence: total configurations g_n = sum_{k=1}^n f_k * c_{n, k} * g_{n-k}, where f_k is the number of strongly connected configurations of size k. This recurrence has convolution form, solvable in O(N log^2 N) time via divide-and-conquer NTT (CDQ NTT).
- Common Reductions: In a bipartite graph with directed edges defined by pairing conditions, count configurations that result in a strongly connected graph modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc196_c`](../../analysis/AtCoder-arc196_c.md) | C. Strongly Connected | 2917 | In a bipartite graph with directed edges defined by pairing conditions, count configurations that result in a strongly c... |
