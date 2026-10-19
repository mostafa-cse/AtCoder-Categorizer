# Prufer Code

**Taxonomy Path**: `Graph Theory` > `Graph Counting` > `Prufer Code`

## Description
This topic focuses on prufer code techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In a directed graph where every vertex has out-degree 1, the number of connected components equals the number of directed cycles. Fixed edges form components of known structure: any fixed cycle contributes to all (N-1)^K states, while the remaining components contract into K trees of sizes s_1..s_K rooted at the free nodes. A new cycle through L free nodes can be formed in (L-1)! * prod s_{i_j} ways. The sum over all L-subsets reduces to the L-th elementary symmetric polynomial of {s_i}, computable via O(K^2) DP.
- Common Reductions: In a functional graph of N cities where K cities choose their outgoing edge uniformly at random among the other N-1 cities, find the expected number of connected components times (N-1)^K modulo 1000000007.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-nomura2020_d`](../../analysis/AtCoder-nomura2020_d.md) | D - Urban Planning | 2810 | In a functional graph of N cities where K cities choose their outgoing edge uniformly at random among the other N-1 citi... |
