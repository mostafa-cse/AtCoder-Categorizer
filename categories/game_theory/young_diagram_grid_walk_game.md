# Grundy Number and Basic Game Theory

**Taxonomy Path**: `Game Theory` > `Grundy Number / Nim` > `Grundy Number and Basic Game Theory`

## Description
This topic focuses on grundy number and basic game theory techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Sort piles in descending order to form a Young diagram. Removing the largest pile shifts origin right (x -> x+1); decrementing all piles shifts origin up (y -> y+1). The game is an impartial grid walk starting at (0, 0) where leaving the diagram loses. Along any diagonal x + y = c, winning/losing outcomes alternate. Find the largest diagonal cell (k, k) inside the diagram. The outcome of (k, k) depends on the parity of the distance to the right boundary vs top boundary.
- Common Reductions: N piles of candies are given. In each turn, a player either removes the largest pile or removes 1 candy from every positive pile. The player who takes the last candy wins. Determine First or Second win.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc002_e`](../../analysis/AtCoder-agc002_e.md) | E. Candy Piles | 2889 | N piles of candies are given. In each turn, a player either removes the largest pile or removes 1 candy from every posit... |
