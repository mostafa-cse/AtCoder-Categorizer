# Subset Convolution

**Taxonomy Path**: `Dynamic Programming (DP)` > `Bit Related DP` > `Subset Convolution`

## Description
This topic focuses on subset convolution techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The probability that the graph is a forest with K edges is g_K(V) * K! / M^K, where g_K(V) is the number of forests with K edges on vertex set V. For each subset S, the number of spanning trees f(S) on the induced subgraph is given by the Matrix Tree Theorem via the determinant of the (|S|-1) x (|S|-1) Laplacian matrix. The number of forests g_i(S) with i edges satisfies the subset convolution DP: g_i(S) = sum_{v in T subset S} f(T) * g_{i - (|T| - 1)}(S \ T), where v is a fixed canonical vertex (e.g. lsb(S)) to avoid overcounting components.
- Common Reductions: Starting with an empty graph on N vertices (N <= 14), we add an edge chosen uniformly at random from a multiset of M edges N-1 times. For each K in 1..N-1, find the probability modulo 998244353 that the graph is a forest after the K-th operation.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc253_h`](../../analysis/AtCoder-abc253_h.md) | Ex - We Love Forest | 2758 | Starting with an empty graph on N vertices (N <= 14), we add an edge chosen uniformly at random from a multiset of M edg... |
