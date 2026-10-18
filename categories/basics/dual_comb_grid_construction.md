# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Since purple cells are strictly internal (not on the boundary $i=1,H$ or $j=1,W$), Red and Blue can be given disjoint interlocking spanning combs: Red spans column 1 and all odd rows (excluding column $W$); Blue spans column $W$ and all even rows (excluding column 1). Red base and Blue base are completely disjoint; adding all purple cells to both ensures Red and Blue remain connected while their intersection is strictly the purple cells.
- Common Reductions: Paint Red and Blue connected grids whose intersection is strictly the given purple cells. Dual interlocking comb construction: Red spans column 1 and all odd rows; Blue spans column $W$ and all even rows. Their base combs are disjoint, solved in $O(HW)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc004_c`](../../analysis/AtCoder-agc004_c.md) | C. AND Grid | 2367 | Paint Red and Blue connected grids whose intersection is strictly the given purple cells. Dual interlocking comb constru... |
