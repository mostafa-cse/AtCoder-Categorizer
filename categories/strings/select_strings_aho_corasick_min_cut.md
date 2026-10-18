# Aho Corasick

**Taxonomy Path**: `Strings` > `Aho Corasick` > `Aho Corasick`

## Description
This topic focuses on aho corasick techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The substring relation forms a partially ordered set (poset). A good subset is an antichain. By Dilworth's theorem and the Picard/Balinski reduction, the maximum weight antichain equals the total weight minus the minimum cut in a bipartite network: source -> L_i with capacity A_i, R_i -> sink with capacity A_i, and infinite capacity edges L_i -> R_j whenever S_i is a substring of S_j (i != j).
- Common Reductions: Finding the maximum weight subset of strings where no string is a substring of another reduces to the Maximum Weight Antichain in a Poset, solvable via Min-Cut on a bipartite flow network.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc354_g`](../../analysis/AtCoder-abc354_g.md) | Select Strings | 2665 | Finding the maximum weight subset of strings where no string is a substring of another reduces to the Maximum Weight Ant... |
