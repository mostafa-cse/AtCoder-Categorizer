# DP Optimization using Data Structures [Some Practice Problems]

**Taxonomy Path**: `Dynamic Programming (DP)` > `DP Optimizations` > `DP Optimization using Data Structures [Some Practice Problems]`

## Description
This topic focuses on dp optimization using data structures [some practice problems] techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each robot between exit A and exit B exits through A iff the left movement reaches x_i - A before the right movement reaches B - x_i. This assigns each robot a threshold pair (a_i, b_i). A subset of robots choosing A vs B corresponds to non-dominated paths in the (a, b) plane. Sorting points by a_i ascending and b_i descending reduces the problem to counting strictly increasing subsequences, solvable via coordinate compression and a Binary Indexed Tree (BIT).
- Common Reductions: N robots and M exits on a line. In each step, all robots move 1 unit left or 1 unit right. A robot exits when reaching an exit. Count the number of possible sets of which robot exits where.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc101_d`](../../analysis/AtCoder-arc101_d.md) | D. Robots and Exits | 2930 | N robots and M exits on a line. In each step, all robots move 1 unit left or 1 unit right. A robot exits when reaching a... |
