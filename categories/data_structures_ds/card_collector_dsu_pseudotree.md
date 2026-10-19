# DSU / Union Find

**Taxonomy Path**: `Data Structures (DS)` > `Disjoint Set Union (DSU)` > `DSU / Union Find`

## Description
This topic focuses on dsu / union find techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A bipartite graph can be directed so all in-degrees <= 1 if and only if each component has at most as many edges as vertices (each component is a tree or a unicyclic pseudo-tree). By the greedy matroid property, sorting edges in descending order of value A_i and adding an edge whenever it does not create a component with >= 2 cycles yields the maximum possible total weight.
- Common Reductions: Each card at (R_i, C_i) represents an edge between row vertex R_i and column vertex H + C_i. A selection of cards is valid if each card can be assigned to either its row or column such that no row/column vertex receives more than 1 card. This is equivalent to orienting edges so that all in-degrees <= 1, which characterizes the bicircular matroid where every connected component has |E| <= |V| (at most 1 cycle per component). We solve this greedily using DSU with cycle tracking.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-jsc2019_qual_e`](../../analysis/AtCoder-jsc2019_qual_e.md) | Card Collector | 2691 | Each card at (R_i, C_i) represents an edge between row vertex R_i and column vertex H + C_i. A selection of cards is val... |
