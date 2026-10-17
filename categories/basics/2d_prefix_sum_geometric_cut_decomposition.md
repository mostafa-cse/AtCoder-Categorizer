# 2D Prefix Sum

**Taxonomy Path**: `Basics` > `2D Prefix Sum` > `2D Prefix Sum`

## Description
This topic focuses on 2d prefix sum techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Computing 2D prefix sums allows evaluating the sum of any M x M square S[i][j] in O(1). Precomputing the 4 corner 2D prefix/suffix maximums (TL, TR, BL, BR) and 1D horizontal/vertical slab maximums enables evaluating all 6 separation topologies in O(N^2) total time.
- Common Reductions: Select three pairwise disjoint M x M squares in an N x N grid to maximize their total element sum. By geometric separating lines, any three non-overlapping squares can be separated by either two parallel cuts (3 horizontal or 3 vertical slabs) or one primary cut and one secondary perpendicular cut (T-splits in 4 orientations: left, right, top, bottom).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc347_f`](../../analysis/AtCoder-abc347_f.md) | I. Non-overlapping Squares | 2179 | Select three pairwise disjoint M x M squares in an N x N grid to maximize their total element sum. By geometric separati... |
