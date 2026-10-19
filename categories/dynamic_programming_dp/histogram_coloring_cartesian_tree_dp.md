# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In any 2x2 square, having two red and two blue squares implies that if two adjacent cells in a row have the same color, the entire column above and below them must alternate colors vertically. Columns naturally form blocks organized in a Cartesian tree by height. For a histogram segment of width w and common baseline height offset x, we define two DP states: dp1 (number of colorings where all columns alternate vertically) and dp2 (colorings where at least one pair of adjacent columns does not alternate vertically). For a block with children c_1, ..., c_k, the transitions are: dp1 = 2^x * prod(dp1_{c_i}), and dp2 = 2^w * prod(dp1_{c_i} + dp2_{c_i}) + (2^x - 2) * prod(dp1_{c_i}).
- Common Reductions: Given a histogram with N columns of heights h_1, ..., h_N, we want to color each 1x1 square red or blue such that in every 2x2 square completely contained in the histogram, there are exactly two red squares and two blue squares. Find the number of valid colorings modulo 10^9 + 7.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc026_d`](../../analysis/AtCoder-agc026_d.md) | D - Histogram Coloring | 2742 | Given a histogram with N columns of heights h_1, ..., h_N, we want to color each 1x1 square red or blue such that in eve... |
