# Bellman Ford

**Taxonomy Path**: `Graph Theory` > `Shortest Paths` > `Bellman Ford`

## Description
This topic focuses on bellman ford techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because all patterns $T_i$ have length $\le 3$, substring matches depend solely on the 2-character suffix of the current string. Constructing a de Bruijn state graph on strings of length $\le 2$ (703 states) maps the maximum beauty problem to the longest walk in a directed graph. A reachable positive cycle yields Infinity; otherwise, the longest walk is finite.
- Common Reductions: Find the maximum beauty of a string scored by matches of patterns of length $\le 3$. Construct a de Bruijn graph on 703 2-letter states; detect positive cycles and find the longest path via SPFA / Bellman-Ford in $O(V \cdot E)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc264_g`](../../analysis/AtCoder-abc264_g.md) | G. String Fair | 2348 | Find the maximum beauty of a string scored by matches of patterns of length $\le 3$. Construct a de Bruijn graph on 703 ... |
