# Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum

**Taxonomy Path**: `Data Structures (DS)` > `Monotonic Data Structures` > `Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum`

## Description
This topic focuses on monotonic stack: all nearest smaller values and all subarray maximum/minimum techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: As R increases, the suffix maximum max(A_{j+1..R}) for each j is piecewise constant and maintained by a monotonic decreasing stack of values. When A_R arrives, popping smaller elements corresponds to range addition on the segment tree, updating A_j + max(A_{j+1..R}). Queries are answered with range minimum query on [m+1, R-1].
- Common Reductions: Partitioning A[L..R] into 3 subarrays to minimize sum of maximums. The global maximum A_m in A[L..R] must fall into one of the 3 parts: if in the middle, cost is A_L + A_m + A_R; if in the left part, the middle part can be taken as a single element A_j, yielding min_{j=m+1..R-1} (A_m + A_j + max(A_{j+1..R})). Symmetrically for the right part. We solve the range query using offline sweep-line with a monotonic stack and range-add range-min segment tree.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc180_d`](../../analysis/AtCoder-arc180_d.md) | Division into 3 | 2694 | Partitioning A[L..R] into 3 subarrays to minimize sum of maximums. The global maximum A_m in A[L..R] must fall into one ... |
