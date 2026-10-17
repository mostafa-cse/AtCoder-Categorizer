# BIT / Fenwick Tree

**Taxonomy Path**: `Data Structures (DS)` > `Binary Indexed Tree (BIT)` > `BIT / Fenwick Tree`

## Description
This topic focuses on bit / fenwick tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For an element x = P[i], its contribution to inversions (elements greater than x to its left, inv_x) decreases by exactly 1 on every operation k that covers x (A_t >= pos(x)) until inv_x reaches 0. Since A is non-decreasing, x becomes covered at operation l_x = lower_bound(A, pos(x)) and decreases by 1 for operations in [l_x, min(M, l_x + inv_x - 1)]. A difference array over operation indices efficiently tracks cumulative inversion drops.
- Common Reductions: Compute the inversion number of a permutation after each step in a sequence of bubble sort passes on prefixes of non-decreasing lengths A_1 <= A_2 <= ... <= A_M.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc181_d`](../../analysis/AtCoder-arc181_d.md) | Prefix Bubble Sort | 2227 | Compute the inversion number of a permutation after each step in a sequence of bubble sort passes on prefixes of non-dec... |
