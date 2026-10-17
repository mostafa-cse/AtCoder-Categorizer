# Interval DP / Range DP / Matrix Chain Multiplication (MCM)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Classic DP` > `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`

## Description
This topic focuses on interval dp / range dp / matrix chain multiplication (mcm) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: When the first machine inside a bounding box [x1, x2] x [y1, y2] is activated at (X_i, Y_i), it collects all gold in its row and column within the box, collecting (x2 - x1 + 1) + (y2 - y1 + 1) - 1 gold. This laser divides the remaining gold into four completely independent sub-rectangles: Top-Left, Top-Right, Bottom-Left, and Bottom-Right.
- Common Reductions: 2D Divide-and-Conquer Range DP decomposing activated machines into four independent rectangular sub-regions.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc008_4`](../../analysis/AtCoder-abc008_4.md) | 金塊ゲーム | 2203 | 2D Divide-and-Conquer Range DP decomposing activated machines into four independent rectangular sub-regions.... |
