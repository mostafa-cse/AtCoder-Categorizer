# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By linearity of expectation, an operation is performed on a connected component S of size > K if and only if that component exists at some point during the process. For a subset of vertices S forming a connected component, S exists if and only if all external neighbors of S in the tree are deleted after all internal vertices of S. If S has n internal vertices and m boundary neighbor vertices, this probability is n! * m! / (n + m)!. We can iterate over every vertex r as the highest (root) vertex of S, and run tree knapsack DP to sum the probabilities over all valid subsets of size > K.
- Common Reductions: In a tree with N vertices, vertices are deleted uniformly at random one by one until all connected components have size at most K. Find the expected number of deletion operations performed, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc165_e`](../../analysis/AtCoder-arc165_e.md) | E - Random Resettlement | 2783 | In a tree with N vertices, vertices are deleted uniformly at random one by one until all connected components have size ... |
