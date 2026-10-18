# Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum

**Taxonomy Path**: `Data Structures (DS)` > `Monotonic Data Structures` > `Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum`

## Description
This topic focuses on monotonic stack: all nearest smaller values and all subarray maximum/minimum techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Inverting a row or column preserves the XOR parity of '#' squares in every 2x2 subgrid. A subgrid can be made all black iff every 2x2 block in it has even parity. A rectangle of a x b valid 2x2 blocks corresponds to an original subgrid of area (a + 1)(b + 1).
- Common Reductions: Given an H x W grid of black and white squares, you can invert any row or column. Find the maximum area of a subgrid that can be made entirely black.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc081_d`](../../analysis/AtCoder-arc081_d.md) | F. Flip and Rectangles | 2608 | Given an H x W grid of black and white squares, you can invert any row or column. Find the maximum area of a subgrid tha... |
