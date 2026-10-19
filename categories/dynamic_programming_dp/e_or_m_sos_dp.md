# Bitmask DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Bit Related DP` > `Bitmask DP`

## Description
This topic focuses on bitmask dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each column can extend 1s from the top down. A grid profile after processing rows 1..i is represented by a bitmask of length M, where the j-th bit is 1 iff column j can still extend 1s downwards. For row i, we transition by choosing a prefix of row 1s up to some column j, which sets a prefix of row i to 1 and places a subset of the column continuation mask for the remaining columns. This subset transition can be performed across all masks using Sum Over Subsets (SOS) / fast zeta transform in O(2^M * M) per row, incorporating the grid constraints ('0'/'1') on what can be placed.
- Common Reductions: Given an N x M grid X with characters in {'0', '1', '?'}, where N, M <= 18. Count how many completions of '?' can be obtained by taking a grid of all 0s, painting a prefix of 1s in each row, and painting a prefix of 1s in each column, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc295_h`](../../analysis/AtCoder-abc295_h.md) | Ex - E or m | 2728 | Given an N x M grid X with characters in {'0', '1', '?'}, where N, M <= 18. Count how many completions of '?' can be obt... |
