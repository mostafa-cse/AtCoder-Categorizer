# Articulation Points and Block Cut Tree

**Taxonomy Path**: `Graph Theory` > `Graph Connectivity` > `Articulation Points and Block Cut Tree`

## Description
This topic focuses on articulation points and block cut tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any two circuits cannot share an edge or vertex because their symmetric difference would form a composite circuit (even length > 2). Hence the block-cut tree must be a tree of isolated vertices and prime-length simple cycles. By Extended Cayley's Theorem, the exponential generating function is G(x) = (1/N^2) \exp(N x + (N/2) \sum_{p >= 3, p \in P} x^p). Computing [x^N] \exp(P(x)) via CDQ divide-and-conquer NTT online convolution yields an exact O(N \log^2 N) solution.
- Common Reductions: Find the number of simple connected graphs on N labeled vertices such that every circuit has a prime number of edges, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc387_g`](../../analysis/AtCoder-abc387_g.md) | G - Prime Circuit | 2986 | Find the number of simple connected graphs on N labeled vertices such that every circuit has a prime number of edges, mo... |
