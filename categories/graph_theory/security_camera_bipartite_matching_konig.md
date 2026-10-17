# Konig's Theorem and Maximum Independent Set in Bipartite Graphs

**Taxonomy Path**: `Graph Theory` > `Matching` > `Konig's Theorem and Maximum Independent Set in Bipartite Graphs`

## Description
This topic focuses on konig's theorem and maximum independent set in bipartite graphs techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each surveillance camera covers at most one maximal horizontal or vertical segment of empty cells. Every empty cell $(r, c)$ must be covered by its row segment or its column segment, reducing the problem to Minimum Vertex Cover in a bipartite graph.
- Common Reductions: Find the minimum number of surveillance cameras to monitor all empty cells in a grid with obstacles. Each camera covers a maximal row or column segment, reducing by König's theorem to maximum bipartite matching via Hopcroft-Karp in $O(HW \sqrt{HW})$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc274_g`](../../analysis/AtCoder-abc274_g.md) | G. Security Camera 3 | 2340 | Find the minimum number of surveillance cameras to monitor all empty cells in a grid with obstacles. Each camera covers ... |
