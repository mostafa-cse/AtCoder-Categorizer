# Maximum Flow / Minimum Cut

**Taxonomy Path**: `Graph Theory` > `Flow and Min Cut` > `Maximum Flow / Minimum Cut`

## Description
This topic focuses on maximum flow / minimum cut techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: On a bipartite grid, inverting labels on one partition transforms a dissimilarity maximization problem into a standard Potts model / minimum cut problem where adjacent pairs with different values pay a unit penalty.
- Common Reductions: Maximize zebraness (adjacent pairs with different colors) on an $N \times N$ grid of 'B', 'W', and '?'. Flip colors on odd chessboard cells: odd 'B' becomes 'W', and odd 'W' becomes 'B'. In the flipped grid, different adjacent colors become identical colors. Maximizing identical adjacent pairs is equivalent to minimizing different adjacent pairs, which is solved by standard Minimum Cut on a flow network.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc193_f`](../../analysis/AtCoder-abc193_f.md) | F. Zebraness | 2475 | Maximize zebraness (adjacent pairs with different colors) on an $N \times N$ grid of 'B', 'W', and '?'. Flip colors on o... |
