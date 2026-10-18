# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each step (i, j) -> (i, j+1) increases 3X+Y by 1, while (i, j) -> (i+1, j-2) also increases 3X+Y by 1. A continuous walk from (1, 1) to (N, M) covering width-3/5 diagonal bands ensures all 3X+Y and X+3Y values are distinct.
- Common Reductions: Select the maximum number of grid cells (X, Y) in an N x M grid such that all X + 3Y are distinct and all 3X + Y are distinct. Theoretical upper bound 3*min(N, M) + max(N, M) - 3 (minus 1 if N=M even) is achieved via an optimal snake-like serpentine walk.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc139_c`](../../analysis/AtCoder-arc139_c.md) | C. One Three Nine | 2406 | Select the maximum number of grid cells (X, Y) in an N x M grid such that all X + 3Y are distinct and all 3X + Y are dis... |
