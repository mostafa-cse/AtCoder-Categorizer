# Maximum Closure Problem

**Taxonomy Path**: `Graph Theory` > `Flow and Min Cut` > `Maximum Closure Problem`

## Description
This topic focuses on maximum closure problem techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Selecting row i imposes a penalty equal to the sum of negative cards in row i; selecting col j imposes a penalty equal to negative cards in col j. Choosing neither incurs an opportunity loss of A_{i,j} for positive cards, and choosing both for a negative card is strictly forbidden (infinite capacity).
- Common Reductions: Maximize score in grid row/column selection with negative card conflicts by starting from the sum of all positive cards and subtracting the minimum s-t cut in a bipartite closure network.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc259_g`](../../analysis/AtCoder-abc259_g.md) | Grid Card Game | 2428 | Maximize score in grid row/column selection with negative card conflicts by starting from the sum of all positive cards ... |
