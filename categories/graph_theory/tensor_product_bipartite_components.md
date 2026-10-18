# Depth First Search (DFS)

**Taxonomy Path**: `Graph Theory` > `Graph Traversal` > `Depth First Search (DFS)`

## Description
This topic focuses on depth first search (dfs) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In the tensor product graph $G \times G$, pairs $(a, b)$ with an isolated vertex in $G$ form isolated vertices in $G \times G$, yielding $I(2N - I)$ components. For non-isolated connected components $C_i, C_j$: if both are bipartite, $C_i \times C_j$ splits into 2 connected components (preserving color parity agreement/disagreement); if at least one is non-bipartite, $C_i \times C_j$ forms exactly 1 connected component because odd cycles allow arbitrary walk length parities.
- Common Reductions: Count connected components in the tensor product graph $G \times G$. Isolated vertices yield $I(2N - I)$ components; bipartite component pairs produce 2 components each, while any pair containing a non-bipartite component forms 1 component, evaluated via DFS in $O(N + M)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc011_c`](../../analysis/AtCoder-agc011_c.md) | C. Squared Graph | 2355 | Count connected components in the tensor product graph $G \times G$. Isolated vertices yield $I(2N - I)$ components; bip... |
