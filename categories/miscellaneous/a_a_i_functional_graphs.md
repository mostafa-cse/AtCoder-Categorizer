# Functional Graphs

**Taxonomy Path**: `Miscellaneous` > `General` > `Functional Graphs`

## Description
This topic focuses on functional graphs techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In the optimal assignment, Snuke only ever writes at most two distinct values: 1 and p, where p is the minimum index such that A_p = 1. If A_1 can be 1 (either A_1 = 1 or A_1 = -1), setting p = 1 and all -1 to 1 achieves B_i = 1 everywhere possible with zero penalty. When A_1 > 1, setting A_i = p makes B_i = A_p = 1, while the chosen pivot index p suffers B_p = A_1 > 1. To make B lexicographically smallest, we delay choosing p as late as possible, until some index i has B_i = p (requiring p to be minimized immediately).
- Common Reductions: Given an array A of length N with elements in {1, ..., N} U {-1}, replace all -1 with integers in {1, ..., N} to make the sequence B defined by B_i = A_{A_i} lexicographically smallest.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc209_d`](../../analysis/AtCoder-arc209_d.md) | D. A_A_i | 2583 | Given an array A of length N with elements in {1, ..., N} U {-1}, replace all -1 with integers in {1, ..., N} to make th... |
