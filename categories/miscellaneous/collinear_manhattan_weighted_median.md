# Ternary Search

**Taxonomy Path**: `Miscellaneous` > `Search Techniques` > `Ternary Search`

## Description
This topic focuses on ternary search techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Perturbed points (A_i + c_i, B_i + d_i) lie on a line through the origin. The minimum Manhattan distance from (A_i, B_i) to line Y = s X (|s| <= 1) is |B_i - s A_i|, and to X = t Y (|t| <= 1) is |A_i - t B_i|. Both reduce to finding the weighted median of critical slope ratios in [-1, 1], evaluated exactly using __int128 rational arithmetic.
- Common Reductions: Given points (A_i, B_i), minimize sum of Manhattan perturbations |c_i| + |d_i| such that all points become collinear through the origin. The Manhattan distance to line Y = s X (|s| <= 1) is |B_i - s A_i|, and to X = t Y (|t| <= 1) is |A_i - t B_i|. Both reduce to weighted median problems on rational slopes, solved with __int128 exact arithmetic in O(N log N) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc479_g`](../../analysis/AtCoder-abc479_g.md) | G. Tuning | 2386 | Given points (A_i, B_i), minimize sum of Manhattan perturbations |c_i| + |d_i| such that all points become collinear thr... |
