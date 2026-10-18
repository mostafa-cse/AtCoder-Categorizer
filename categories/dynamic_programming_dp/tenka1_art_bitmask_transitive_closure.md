# Bitmask DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Bit Related DP` > `Bitmask DP`

## Description
This topic focuses on bitmask dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each color i must cover a bounding box [L_i, R_i] x [T_i, B_i]. If another color j overlaps inside color i's bounding box, color j must have been painted strictly after color i. This defines a directed dependency graph. Furthermore, colors with identical sizes can be assigned to brush dimensions. We compute the transitive closure of dependencies to check for cycles, and then use bitmask dynamic programming over subset configurations to match colors to sizes.
- Common Reductions: Given an N x N target grid painted with N overlapping rectangular brush strokes and a list of brush sizes A_i, determine whether the target grid could have been produced by painting rectangles of sizes A_i in some order.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-tenka1_2014_qualB_d`](../../analysis/AtCoder-tenka1_2014_qualB_d.md) | D. 天下一芸術 (Tenka1 Art) | 2572 | Given an N x N target grid painted with N overlapping rectangular brush strokes and a list of brush sizes A_i, determine... |
