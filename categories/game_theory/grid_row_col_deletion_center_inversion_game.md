# Grundy Number and Basic Game Theory

**Taxonomy Path**: `Game Theory` > `Grundy Number / Nim` > `Grundy Number and Basic Game Theory`

## Description
This topic focuses on grundy number and basic game theory techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Analyze the geometry of shrinking the rectangle around the grid center. If one dimension is odd and the other is even, the game directly reduces to whether the central column/row has a '1' or whether the center forms a specific alternating cross structure. When both dimensions have the same parity, the first move transitions into an odd-even subgrid with inverted polarity. Thus, the winning condition decomposes into checking the central cross cells and testing the 4 single-boundary reductions in O(1) per state.
- Common Reductions: Two players play an impartial game on an H x W binary grid. A player can remove an entire boundary row/column if its sum is non-zero. Determine who wins under optimal play across T testcases.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc207_d`](../../analysis/AtCoder-arc207_d.md) | D - Devourers and Cake | 2957 | Two players play an impartial game on an H x W binary grid. A player can remove an entire boundary row/column if its sum... |
