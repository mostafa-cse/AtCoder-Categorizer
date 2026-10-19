# DSU / Union Find

**Taxonomy Path**: `Data Structures (DS)` > `Disjoint Set Union (DSU)` > `DSU / Union Find`

## Description
This topic focuses on dsu / union find techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Allowed swaps form transpositions that generate the full symmetric group S_{|C|} on each connected component C. The number of distinct color arrangements is prod_C (|C|! / prod_{c in C} cnt_C[c]!). To efficiently build the graph, for balls of the same color, it suffices to connect each ball i to the minimum-weight ball of color c_i. For balls of different colors, let B_1 be the globally minimum-weight ball (color c_1) and B_2 be the minimum-weight ball of any other color. Connecting each ball with color != c_1 to B_1 (if w_i + w(B_1) <= Y) and each ball with color == c_1 to B_2 (if w_i + w(B_2) <= Y) captures all connected components in O(N alpha(N)) time using DSU.
- Common Reductions: N balls have colors c_i and weights w_i. Two balls of the same color can swap if w_i + w_j <= X. Two balls of different colors can swap if w_i + w_j <= Y. Find the number of distinct color arrangements modulo 10^9 + 7.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc012_d`](../../analysis/AtCoder-agc012_d.md) | D - Colorful Balls | 2760 | N balls have colors c_i and weights w_i. Two balls of the same color can swap if w_i + w_j <= X. Two balls of different ... |
