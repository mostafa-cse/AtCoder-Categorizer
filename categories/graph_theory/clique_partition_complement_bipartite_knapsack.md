# Maximum Clique

**Taxonomy Path**: `Graph Theory` > `Cliques and Independent Sets` > `Maximum Clique`

## Description
This topic focuses on maximum clique techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Two vertices belong to the same clique in G iff there is NO edge between them in the complement graph G_bar. Thus, the complement graph must be bipartite; otherwise no valid partition exists (output -1). For each bipartite connected component with partition sizes (s_i, t_i), choose one side for state A using knapsack DP, minimizing same-state edges C(a, 2) + C(b, 2).
- Common Reductions: Partition a graph into two cliques minimizing edges with endpoints in the same state. A clique partition in G corresponds to a 2-coloring (bipartite coloring) in the complement graph G_bar. Knapsack balances the component color classes.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| `[problem:AtCoder-arc099_c]` | Independence | 2160 | Partition a graph into two cliques minimizing edges with endpoints in the same state. A clique partition in G correspond... |
