# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If no cell is black initially, it is impossible (output -1). If all cells are black, 0 operations. Every column not initially full black must eventually be painted by an all-black row. To make row r all black, for each white cell (r, c) we copy a row whose r-th cell is black into column c (Z_r operations). If column r has no black cell initially, 1 extra operation seeds column r with a black cell.
- Common Reductions: On an N x N grid of white/black cells, an operation copies row i into column j. Minimize operations to make all cells black. The strategy is to construct a single completely black row r, and then copy row r into every column that is not already fully black. Solved by iterating over all possible target rows r.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-mujin_pc_2017_b`](../../analysis/AtCoder-mujin_pc_2017_b.md) | B. Row to Column | 2177 | On an N x N grid of white/black cells, an operation copies row i into column j. Minimize operations to make all cells bl... |
