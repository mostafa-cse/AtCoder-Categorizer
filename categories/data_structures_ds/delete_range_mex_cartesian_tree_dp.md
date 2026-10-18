# Cartesian Tree

**Taxonomy Path**: `Data Structures (DS)` > `More Tree Data Structures` > `Cartesian Tree`

## Description
This topic focuses on cartesian tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The condition corresponds to Cartesian tree insertion: elements not in $A$ must be inserted strictly outside the span of currently placed smaller elements. Tracking $l$ and $r$ as the remaining unplaced elements of $A$ to the left and right, placing element $i \notin A$ splits into transitions $(l, r) \to (l', r)$ or $(l, r')$. These transitions can be updated in $O(M^2)$ using 2D prefix sums.
- Common Reductions: Count permutations $P$ of $(0, 1, \dots, N-1)$ containing sequence $A$ as a subsequence such that repeatedly deleting range minimum / MEX reduces to valid intervals.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc178_d`](../../analysis/AtCoder-arc178_d.md) | D. Delete Range Mex | 2498 | Count permutations $P$ of $(0, 1, \dots, N-1)$ containing sequence $A$ as a subsequence such that repeatedly deleting ra... |
