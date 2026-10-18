# Bipartite Matching (HopCroft Karp Algorithm and Kuhn's Algorithm)

**Taxonomy Path**: `Graph Theory` > `Matching` > `Bipartite Matching (HopCroft Karp Algorithm and Kuhn's Algorithm)`

## Description
This topic focuses on bipartite matching (hopcroft karp algorithm and kuhn's algorithm) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Model products as vertices in a directed graph G, with an edge u -> v if the 2nd character of u equals the 1st character of v. Strings in the NG list correspond to directed walks. Compacting G into its SCC condensation DAG G', the problem reduces to finding the minimum path cover on G'. By Dilworth's theorem, minimum path cover equals V' - max_bipartite_matching.
- Common Reductions: Given N 2-letter uppercase product names, construct the minimum number of strings such that each product appears as a substring, and no unused length-2 substring is formed.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc374_g`](../../analysis/AtCoder-abc374_g.md) | G. Only One Product Name | 2608 | Given N 2-letter uppercase product names, construct the minimum number of strings such that each product appears as a su... |
