# BIT / Fenwick Tree

**Taxonomy Path**: `Data Structures (DS)` > `Binary Indexed Tree (BIT)` > `BIT / Fenwick Tree`

## Description
This topic focuses on bit / fenwick tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Normalizing lines to B_i > 0, the y-value at x = X is (C_i - A_i X) / B_i. Sorting lines by slope m_i = -A_i / B_i ascending, line i and j (with i < j) cross at or before X iff y_i(X) <= y_j(X). Counting pairs (i, j) with i < j and y_i <= y_j is standard inversion counting via merge sort.
- Common Reductions: Minimizing sum of Manhattan distances to N(N-1)/2 intersection points decouples into 1D median problems for X and Y independently. The number of intersection points with x_coord <= X is equal to the number of line pairs whose vertical order at x = X is inverted relative to x -> -infinity (i.e. sorted by slope). We count intersections in O(N log N) using merge sort / BIT, allowing binary search for the median coordinate in O(N log N log(range)).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-tenka1_2017_e`](../../analysis/AtCoder-tenka1_2017_e.md) | CAR CAR CAR | 2703 | Minimizing sum of Manhattan distances to N(N-1)/2 intersection points decouples into 1D median problems for X and Y inde... |
