# Cartesian Tree

**Taxonomy Path**: `Data Structures (DS)` > `More Tree Data Structures` > `Cartesian Tree`

## Description
This topic focuses on cartesian tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Decompose the array using Cartesian Tree / RMQ Divide and Conquer. For a subarray [L, R] with minimum at m, any pair spanning m satisfies sum_{k=l}^r A_k <= S - A_m. We iterate over the smaller side of the split (small-to-large) and binary search on prefix sums on the larger side, achieving O(N log^2 N) overall time.
- Common Reductions: Given an array A of length N and bound S, count pairs (l, r) with 1 <= l <= r <= N such that min_{l <= k <= r} A_k + sum_{k=l}^r A_k <= S.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc282_h`](../../analysis/AtCoder-abc282_h.md) | Ex - Min + Sum | 2621 | Given an array A of length N and bound S, count pairs (l, r) with 1 <= l <= r <= N such that min_{l <= k <= r} A_k + sum... |
