# Games on Arbitrary Graphs

**Taxonomy Path**: `Game Theory` > `Graph Games` > `Games on Arbitrary Graphs`

## Description
This topic focuses on games on arbitrary graphs techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The game is a finite full-information extensive-form game on a tree, solvable by Minimax DFS. Since path length increases by 1 at each step, running order statistics (median) along the path from root to leaf can be maintained dynamically in O(log N) using a Fenwick tree with binary lifting over coordinate-compressed values.
- Common Reductions: Two players play a game on a tree moving a piece downwards from root 1 to a leaf. Taro maximizes the median of node values visited, Jiro minimizes it. Find the final median score under optimal play.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc218_g`](../../analysis/AtCoder-abc218_g.md) | Game on Tree 2 | 2217 | Two players play a game on a tree moving a piece downwards from root 1 to a leaf. Taro maximizes the median of node valu... |
