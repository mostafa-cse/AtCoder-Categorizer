# Stirling Numbers (Basic)

**Taxonomy Path**: `Combinatorics` > `Stirling Numbers` > `Stirling Numbers (Basic)`

## Description
This topic focuses on stirling numbers (basic) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A multigraph is bipartite iff its underlying simple graph is bipartite. Generating bipartite multigraphs with M edges can be decomposed via the number of connected components and Stirling numbers of the second kind. The number of 2-colored graphs on n vertices with m edges is g(n, m) = sum_i binom(n, i) binom(i(n-i), m). Using polynomial logarithm H = log(G) to extract connected 2-colored graphs, and exponential F = exp(H/2) to eliminate overcounting of 2-colorings, we obtain the counts of bipartite graphs f(n, k) with k edges. The M multigraph edges are mapped to k simple edges via Stirling numbers / inclusion-exclusion.
- Common Reductions: Count sequences of M pairs (u_i, v_i) with 1 <= u_i < v_i <= N such that the resulting multigraph is bipartite, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc327_g`](../../analysis/AtCoder-abc327_g.md) | G - Many Good Tuple Problems | 2968 | Count sequences of M pairs (u_i, v_i) with 1 <= u_i < v_i <= N such that the resulting multigraph is bipartite, modulo 9... |
